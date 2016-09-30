# NOTE: This RPM relies on Internet connection for building,
# and is downloading RubyGems directly from https://rubygems.org
#
%define version 2.4.3
%define release 1
%define rspec_version >= 3.1

Summary: Puppet environment and module deployment
Name: r10k

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: ASL 2.0
URL: https://github.com/puppetlabs/r10k

BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: ruby >= 1.9.3
Requires: rubygems >= 2.0.14
Requires: git
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygems >= 2.0.14
BuildRequires: git
BuildRequires: libgit2-devel
BuildRequires: ruby-devel
BuildRequires: cmake
Provides: ruby(R10k) = %{version}

%description
R10K provides a general purpose toolset for deploying Puppet environments
and modules.
It implements the Puppetfile format and provides a native implementation of
Puppet dynamic environments.

%prep
%setup -T -c

%build
export BUILD_DIR=`pwd`

export GEM_HOME="$BUILD_DIR/rspec"

# Installing rspec, for local testing
gem install rspec --version '%{rspec_version}'

export GEM_PATH="$GEM_HOME:/usr/share/gems"
export GEM_HOME="$BUILD_DIR/ruby"
GEM_PATH="$GEM_HOME:$GEM_PATH"

# Install dist gems
gem install rugged
gem install r10k -v '= %{version}'

cat > r10k.sh <<EOF
#!/bin/sh

export GEM_HOME=/opt/r10k/ruby
exec /opt/r10k/ruby/bin/r10k "\$@"
EOF

%check
export BUILD_DIR=`pwd`
export GEM_PATH="$BUILD_DIR/ruby:$BUILD_DIR/rspec:/usr/share/gems"
PATH="$BUILD_DIR/ruby/bin:$BUILD_DIR/rspec/bin:$PATH"

cd ruby/gems/r10k-%{version}/

rspec spec/unit

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/opt/r10k

%{__cp} -r ruby/ %{buildroot}/opt/r10k/
%{__mkdir} -p %{buildroot}%{_bindir}
%{__cp} r10k.sh %{buildroot}%{_bindir}/r10k
chmod 0755 %{buildroot}%{_bindir}/r10k

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/r10k
/opt/r10k

%changelog
* Thu Sep 29 2016 Markus Frosch <markus.frosch@netways.de> 2.4.3-1
- Initial packaging as bundled gems
