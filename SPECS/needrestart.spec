Name:    needrestart
Version: 2.9
Release: 1%{dist}
Summary: checks which daemons need to be restarted after library upgrades
License: GPL-2.0
URL:     https://fiasko-nw.net/~thomas/tag/needrestart.html

Source0: https://github.com/liske/needrestart/archive/v%{version}.tar.gz

BuildRequires: gettext
BuildRequires: perl-macros
BuildRequires: perl-Proc-ProcessTable
BuildRequires: perl-Sort-Naturally
#BuildRequires:  perl-Term-ProgressBar-Simple
BuildRequires:  perl-Module-Find
BuildRequires:  perl-ExtUtils-MakeMaker

%description
needrestart checks which daemons need to be restarted after library upgrades.
It is inspired by checkrestart from the debian-goodies package.

needrestart supports but does not require systemd (available since v0.6).
If systemd is not available or does not return a service name needrestart
uses hooks to identify the corresponding System V init script.

%define debug_package %{nil}

%prep
%setup -q -n needrestart-%{version}

%build
%{__make}

%install
%{__make} install DESTDIR=%{buildroot}

%{__rm} -f %{buildroot}%{_datadir}/perl5/vendor_perl/NeedRestart/UI/Debconf.pm
%{__rm} -rf %{buildroot}%{_libdir}/perl5/perllocal.pod
%{__rm} -rf %{buildroot}%{_libdir}/perl5/vendor_perl/auto

%files
%config %{_sysconfdir}/needrestart
%{_libdir}/perl5
%{_prefix}/lib/needrestart
%{_sbindir}/needrestart
%{_datadir}/perl5/vendor_perl/NeedRestart
%{_datadir}/perl5/vendor_perl/NeedRestart.pm
%{_datadir}/locale
%{_datadir}/polkit-1/actions/net.fiasko-nw.needrestart.policy

%changelog
* Thu Oct 06 2016 Markus Frosch <markus@lazyfrosch.de>
- Initial package
