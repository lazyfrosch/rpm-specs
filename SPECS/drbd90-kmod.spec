# Define the kmod package name here.
%define kmod_name drbd90
%define real_name drbd

# If kversion isn't defined on the rpmbuild line, define it here.
%{!?kversion: %define kversion 3.10.0-327.28.3.el7.%{_target_cpu}}

Name:    %{kmod_name}-kmod
Version: 9.0.4
Release: 2%{?dist}
Group:   System Environment/Kernel
License: GPLv2
Summary: Distributed Redundant Block Device driver for Linux
URL:     http://www.drbd.org/

BuildRequires: perl
BuildRequires: redhat-rpm-config
BuildRequires: gcc
ExclusiveArch: x86_64

# Sources.
Source0:  http://www.drbd.org/download/drbd/9.0/drbd-%{version}-1.tar.gz
Source10: kmodtool-%{kmod_name}-el7.sh

# Magic hidden here.
%{expand:%(sh %{SOURCE10} rpmtemplate %{kmod_name} %{kversion} "")}

# Disable the building of the debug package(s).
%define debug_package %{nil}

%description
DRBD is a distributed replicated block device. It mirrors a
block device over the network to another machine. Think of it
as networked raid 1. It is a building block for setting up
high availability (HA) clusters.

%prep
%setup -n %{real_name}-%{version}-1
echo "override %{kmod_name} * weak-updates/%{kmod_name}" > kmod-%{kmod_name}.conf

%build
KSRC=%{_usrsrc}/kernels/%{kversion}
%{__make} %{?_smp_mflags} module KDIR=${KSRC} KVER=%{kversion}

%install
%{__install} -d %{buildroot}/lib/modules/%{kversion}/extra/%{kmod_name}/
%{__install} drbd/*.ko %{buildroot}/lib/modules/%{kversion}/extra/%{kmod_name}/
%{__install} -d %{buildroot}%{_sysconfdir}/depmod.d/
%{__install} kmod-%{kmod_name}.conf %{buildroot}%{_sysconfdir}/depmod.d/
for file in ChangeLog COPYING README; do
    %{__install} -Dp -m0644 $file %{buildroot}%{_defaultdocdir}/kmod-%{kmod_name}-%{version}/$file
done

# strip the modules(s)
find %{buildroot} -type f -name \*.ko -exec %{__strip} --strip-debug \{\} \;

# Sign the modules(s)
%if %{?_with_modsign:1}%{!?_with_modsign:0}
# If the module signing keys are not defined, define them here.
%{!?privkey: %define privkey %{_sysconfdir}/pki/SECURE-BOOT-KEY.priv}
%{!?pubkey: %define pubkey %{_sysconfdir}/pki/SECURE-BOOT-KEY.der}
for module in $(find %{buildroot} -type f -name \*.ko);
do %{__perl} /usr/src/kernels/%{kversion}/scripts/sign-file \
sha256 %{privkey} %{pubkey} $module;
done
%endif

%clean
%{__rm} -rf %{buildroot}

%changelog
* Thu Sep 15 2016 Markus Frosch <markus.frosch@netways.de> - 9.0.4-2
- Update kmodtool-drbd90-el7.sh - Package name of utils

* Wed Sep 13 2016 Markus Frosch <markus.frosch@netways.de> - 9.0.4-1
- Update to 9.0.4
- Add gcc BuildRequires

* Wed Jun 24 2015 Hiroshi Fujishima <h-fujishima@sakura.ad.jp> - 9.0.0-1
- Initial el7 build of the kmod package.
