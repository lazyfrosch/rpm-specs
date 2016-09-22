%global _hardened_build 1

Name: monitoring-plugins
Version: 2.1.2
Release: 1%{?dist}
Summary: Host/service/network monitoring program plugins for Nagios/Icinga and compatible

Group: Applications/System
License: GPLv2+
URL: https://www.monitoring-plugins.org/
Source0: https://www.monitoring-plugins.org/download/%{name}-%{version}.tar.gz
Source1: monitoring-plugins.README.Fedora

BuildRequires: gcc
BuildRequires: openldap-devel
BuildRequires: mysql-devel
BuildRequires: net-snmp-devel
BuildRequires: net-snmp-utils
BuildRequires: samba-client
BuildRequires: postgresql-devel
BuildRequires: gettext
BuildRequires: %{_bindir}/ssh
BuildRequires: bind-utils
BuildRequires: ntp
BuildRequires: %{_bindir}/mailq
BuildRequires: %{_sbindir}/fping
BuildRequires: perl(Net::SNMP)
%if 0%{?fedora}
BuildRequires: freeradius-client-devel
%endif
BuildRequires: qstat
BuildRequires: libdbi-devel

Requires: nagios-common >= 3.3.1-1

Obsoletes: monitoring-plugins-linux_raid < 1.4.16-11

# nagios-plugins-1.4.16: the included gnulib files were last updated
# in June/July 2010
# Bundled gnulib exception (https://fedorahosted.org/fpc/ticket/174)
Provides: bundled(gnulib)

Conflicts: nagios-plugins
Obsoletes: nagios-plugins
Provides: nagios-plugins

%global reqfilt sh -c "%{__perl_requires} | sed -e 's!perl(utils)!monitoring-plugins-perl!'"
%global __perl_requires %{reqfilt}


%description
Nagios/Icinga is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios/Icinga runs on a Unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios/Icinga. This package
contains those plugins.

%package all
Summary: Nagios/Icinga Plugins - All plugins
Group: Applications/System
Requires: monitoring-plugins-breeze, monitoring-plugins-by_ssh, monitoring-plugins-dhcp, monitoring-plugins-dig, monitoring-plugins-disk, monitoring-plugins-disk_smb, monitoring-plugins-dns, monitoring-plugins-dummy, monitoring-plugins-file_age, monitoring-plugins-flexlm, monitoring-plugins-fping, monitoring-plugins-hpjd, monitoring-plugins-http, monitoring-plugins-icmp, monitoring-plugins-ide_smart, monitoring-plugins-ircd, monitoring-plugins-ldap, monitoring-plugins-load, monitoring-plugins-log, monitoring-plugins-mailq, monitoring-plugins-mrtg, monitoring-plugins-mrtgtraf, monitoring-plugins-mysql, monitoring-plugins-nagios, monitoring-plugins-nt, monitoring-plugins-ntp, monitoring-plugins-nwstat, monitoring-plugins-oracle, monitoring-plugins-overcr, monitoring-plugins-pgsql, monitoring-plugins-ping, monitoring-plugins-procs, monitoring-plugins-game, monitoring-plugins-real, monitoring-plugins-rpc, monitoring-plugins-smtp, monitoring-plugins-snmp, monitoring-plugins-ssh, monitoring-plugins-swap, monitoring-plugins-tcp, monitoring-plugins-time, monitoring-plugins-ups, monitoring-plugins-users, monitoring-plugins-wave, monitoring-plugins-cluster
%ifnarch ppc ppc64 ppc64p7 sparc sparc64
Requires: monitoring-plugins-sensors
%endif
Conflicts: nagios-plugins-all
Obsoletes: nagios-plugins-all

%description all
This package provides all Nagios/Icinga plugins.

%package apt
Summary: Nagios/Icinga Plugin - check_apt
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-apt
Obsoletes: nagios-plugins-apt

%description apt
Provides check_apt support for Nagios/Icinga.

%package breeze
Summary: Nagios/Icinga Plugin - check_breeze
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-breeze
Obsoletes: nagios-plugins-breeze

%description breeze
Provides check_breeze support for Nagios/Icinga.

%package by_ssh
Summary: Nagios/Icinga Plugin - check_by_ssh
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-by_ssh
Obsoletes: nagios-plugins-by_ssh
Requires: %{_bindir}/ssh

%description by_ssh
Provides check_by_ssh support for Nagios/Icinga.

%package cluster
Summary: Nagios/Icinga Plugin - check_cluster
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-cluster
Obsoletes: nagios-plugins-cluster

%description cluster
Provides check_cluster support for Nagios/Icinga.

%package dbi
Summary: Nagios/Icinga Plugin - check_dbi
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-dbi
Obsoletes: nagios-plugins-dbi

%description dbi
Provides check_dbi support for Nagios/Icinga.

%package dhcp
Summary: Nagios/Icinga Plugin - check_dhcp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-dhcp
Obsoletes: nagios-plugins-dhcp

%description dhcp
Provides check_dhcp support for Nagios/Icinga.

%post dhcp
if command -v setcap > /dev/null; then
    if setcap "cap_net_bind_service=+ep cap_net_raw=+ep" %{_libdir}/nagios/plugins/check_dhcp; then
        echo "Setcap for check_dhcp !"
    else
        echo "Setcap for check_dhcp failed." >&2
        echo "You won't be able to use check_dhcp without root!" >&2
    fi
else
    echo "Setcap is not installed." >&2
    echo "You won't be able to use check_dhcp without root!" >&2
fi


%package dig
Summary: Nagios/Icinga Plugin - check_dig
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-dig
Obsoletes: nagios-plugins-dig
Requires: %{_bindir}/dig

%description dig
Provides check_dig support for Nagios/Icinga.

%package disk
Summary: Nagios/Icinga Plugin - check_disk
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-disk
Obsoletes: nagios-plugins-disk

%description disk
Provides check_disk support for Nagios/Icinga.

%package disk_smb
Summary: Nagios/Icinga Plugin - check_disk_smb
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-disk_smb
Obsoletes: nagios-plugins-disk_smb
Requires: %{_bindir}/smbclient

%description disk_smb
Provides check_disk_smb support for Nagios/Icinga.

%package dns
Summary: Nagios/Icinga Plugin - check_dns
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-dns
Obsoletes: nagios-plugins-dns
Requires: %{_bindir}/nslookup

%description dns
Provides check_dns support for Nagios/Icinga.

%package dummy
Summary: Nagios/Icinga Plugin - check_dummy
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-dummy
Obsoletes: nagios-plugins-dummy

%description dummy
Provides check_dummy support for Nagios/Icinga.
This plugin does not actually check anything, simply provide it with a flag
0-4 and it will return the corresponding status code to Nagios/Icinga.

%package file_age
Summary: Nagios/Icinga Plugin - check_file_age
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-file_age
Obsoletes: nagios-plugins-file_age

%description file_age
Provides check_file_age support for Nagios/Icinga.

%package flexlm
Summary: Nagios/Icinga Plugin - check_flexlm
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-flexlm
Obsoletes: nagios-plugins-flexlm

%description flexlm
Provides check_flexlm support for Nagios/Icinga.

%package fping
Summary: Nagios/Icinga Plugin - check_fping
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-fping
Obsoletes: nagios-plugins-fping
Requires: %{_sbindir}/fping

%description fping
Provides check_fping support for Nagios/Icinga.

%post fping
if command -v setcap > /dev/null; then
    if setcap "cap_net_raw+ep" %{_libdir}/nagios/plugins/check_fping; then
        echo "Setcap for check_fping !"
    else
        echo "Setcap for check_fping failed." >&2
        echo "You won't be able to use check_fping without root!" >&2
    fi
else
    echo "Setcap is not installed." >&2
    echo "You won't be able to use check_fping without root!" >&2
fi

%package game
Summary: Nagios/Icinga Plugin - check_game
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-game
Obsoletes: nagios-plugins-game
Requires: qstat

%description game
Provides check_game support for Nagios/Icinga.

%package hpjd
Summary: Nagios/Icinga Plugin - check_hpjd
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-hpjd
Obsoletes: nagios-plugins-hpjd

%description hpjd
Provides check_hpjd support for Nagios/Icinga.

%package http
Summary: Nagios/Icinga Plugin - check_http
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-http
Obsoletes: nagios-plugins-http

%description http
Provides check_http support for Nagios/Icinga.

%package icmp
Summary: Nagios/Icinga Plugin - check_icmp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-icmp
Obsoletes: nagios-plugins-icmp

%description icmp
Provides check_icmp support for Nagios/Icinga.

%post icmp
if command -v setcap > /dev/null; then
    if setcap "cap_net_raw+ep" %{_libdir}/nagios/plugins/check_icmp; then
        echo "Setcap for check_icmp !"
    else
        echo "Setcap for check_icmp failed." >&2
        echo "You won't be able to use check_icmp without root!" >&2
    fi
else
    echo "Setcap is not installed." >&2
    echo "You won't be able to use check_icmp without root!" >&2
fi

%package ide_smart
Summary: Nagios/Icinga Plugin - check_ide_smart
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-ide_smart
Obsoletes: nagios-plugins-ide_smart

%description ide_smart
Provides check_ide_smart support for Nagios/Icinga.

%package ifoperstatus
Summary: Nagios/Icinga Plugin - check_ifoperstatus
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-ifoperstatus
Obsoletes: nagios-plugins-ifoperstatus

%description ifoperstatus
Provides check_ifoperstatus support for Nagios/Icinga to monitor network interfaces.

%package ifstatus
Summary: Nagios/Icinga Plugin - check_ifstatus
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-ifstatus
Obsoletes: nagios-plugins-ifstatus

%description ifstatus
Provides check_ifstatus support for Nagios/Icinga to monitor network interfaces.

%package ircd
Summary: Nagios/Icinga Plugin - check_ircd
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-ircd
Obsoletes: nagios-plugins-ircd

%description ircd
Provides check_ircd support for Nagios/Icinga.

%package ldap
Summary: Nagios/Icinga Plugin - check_ldap
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-ldap
Obsoletes: nagios-plugins-ldap

%description ldap
Provides check_ldap support for Nagios/Icinga.

%package load
Summary: Nagios/Icinga Plugin - check_load
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-load
Obsoletes: nagios-plugins-load

%description load
Provides check_load support for Nagios/Icinga.

%package log
Summary: Nagios/Icinga Plugin - check_log
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-log
Obsoletes: nagios-plugins-log
Requires: /bin/egrep
Requires: /bin/mktemp

%description log
Provides check_log support for Nagios/Icinga.

%package mailq
Summary: Nagios/Icinga Plugin - check_mailq
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-mailq
Obsoletes: nagios-plugins-mailq
Requires: %{_bindir}/mailq

%description mailq
Provides check_mailq support for Nagios/Icinga.

%package mrtg
Summary: Nagios/Icinga Plugin - check_mrtg
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-mrtg
Obsoletes: nagios-plugins-mrtg

%description mrtg
Provides check_mrtg support for Nagios/Icinga.

%package mrtgtraf
Summary: Nagios/Icinga Plugin - check_mrtgtraf
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-mrtgtraf
Obsoletes: nagios-plugins-mrtgtraf

%description mrtgtraf
Provides check_mrtgtraf support for Nagios/Icinga.

%package mysql
Summary: Nagios/Icinga Plugin - check_mysql
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-mysql
Obsoletes: nagios-plugins-mysql

%description mysql
Provides check_mysql and check_mysql_query support for Nagios/Icinga.

%package nagios
Summary: Nagios/Icinga Plugin - check_nagios
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-nagios
Obsoletes: nagios-plugins-nagios

%description nagios
Provides check_nagios support for Nagios/Icinga.

%package nt
Summary: Nagios/Icinga Plugin - check_nt
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-nt
Obsoletes: nagios-plugins-nt

%description nt
Provides check_nt support for Nagios/Icinga.

%package ntp
Summary: Nagios/Icinga Plugin - check_ntp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-ntp
Obsoletes: nagios-plugins-ntp

%description ntp
Provides check_ntp support for Nagios/Icinga.

%package nwstat
Summary: Nagios/Icinga Plugin - check_nwstat
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-nwstat
Obsoletes: nagios-plugins-nwstat

%description nwstat
Provides check_nwstat support for Nagios/Icinga.

%package oracle
Summary: Nagios/Icinga Plugin - check_oracle
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-oracle
Obsoletes: nagios-plugins-oracle

%description oracle
Provides check_oracle support for Nagios/Icinga.

%package overcr
Summary: Nagios/Icinga Plugin - check_overcr
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-overcr
Obsoletes: nagios-plugins-overcr

%description overcr
Provides check_overcr support for Nagios/Icinga.

%package perl
Summary: Nagios/Icinga plugins perl dep.
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-perl
Obsoletes: nagios-plugins-perl

%description perl
Perl dep for nagios plugins.  This is *NOT* an actual plugin it simply provides
utils.pm

%package pgsql
Summary: Nagios/Icinga Plugin - check_pgsql
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-pgsql
Obsoletes: nagios-plugins-pgsql

%description pgsql
Provides check_pgsql (PostgreSQL)  support for Nagios/Icinga.

%package ping
Summary: Nagios/Icinga Plugin - check_ping
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-ping
Obsoletes: nagios-plugins-ping
Requires: /bin/ping
Requires: /bin/ping6

%description ping
Provides check_ping support for Nagios/Icinga.

%package procs
Summary: Nagios/Icinga Plugin - check_procs
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-procs
Obsoletes: nagios-plugins-procs

%description procs
Provides check_procs support for Nagios/Icinga.

%if 0%{?fedora}
%package radius
Summary: Nagios/Icinga Plugin - check_radius
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-radius
Obsoletes: nagios-plugins-radius

%description radius
Provides check_radius support for Nagios/Icinga.
%endif

%package real
Summary: Nagios/Icinga Plugin - check_real
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-real
Obsoletes: nagios-plugins-real

%description real
Provides check_real (rtsp) support for Nagios/Icinga.

%package rpc
Summary: Nagios/Icinga Plugin - check_rpc
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-rpc
Obsoletes: nagios-plugins-rpc
Requires: %{_sbindir}/rpcinfo

%description rpc
Provides check_rpc support for Nagios/Icinga.

%ifnarch ppc ppc64 sparc sparc64
%package sensors
Summary: Nagios/Icinga Plugin - check_sensors
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-sensors
Obsoletes: nagios-plugins-sensors
Requires: /bin/egrep
Requires: %{_bindir}/sensors

%description sensors
Provides check_sensors support for Nagios/Icinga.
%endif

%package smtp
Summary: Nagios/Icinga Plugin - check_smtp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-smtp
Obsoletes: nagios-plugins-smtp

%description smtp
Provides check_smtp support for Nagios/Icinga.

%package snmp
Summary: Nagios/Icinga Plugin - check_snmp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-snmp
Obsoletes: nagios-plugins-snmp
Requires: %{_bindir}/snmpgetnext
Requires: %{_bindir}/snmpget

%description snmp
Provides check_snmp support for Nagios/Icinga.

%package ssh
Summary: Nagios/Icinga Plugin - check_ssh
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-ssh
Obsoletes: nagios-plugins-ssh

%description ssh
Provides check_ssh support for Nagios/Icinga.

%package swap
Summary: Nagios/Icinga Plugin - check_swap
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-swap
Obsoletes: nagios-plugins-swap

%description swap
Provides check_swap support for Nagios/Icinga.

%package tcp
Summary: Nagios/Icinga Plugin - check_tcp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-tcp
Obsoletes: nagios-plugins-tcp
Provides: monitoring-plugins-ftp = %{version}-%{release}
Provides: monitoring-plugins-imap = %{version}-%{release}
Provides: monitoring-plugins-jabber = %{version}-%{release}
Provides: monitoring-plugins-nntp = %{version}-%{release}
Provides: monitoring-plugins-nntps = %{version}-%{release}
Provides: monitoring-plugins-pop = %{version}-%{release}
Provides: monitoring-plugins-simap = %{version}-%{release}
Provides: monitoring-plugins-spop = %{version}-%{release}
Provides: monitoring-plugins-ssmtp = %{version}-%{release}
Provides: monitoring-plugins-udp = %{version}-%{release}
Provides: monitoring-plugins-udp2 = %{version}-%{release}
Obsoletes: monitoring-plugins-udp < 1.4.15-2

%description tcp
Provides check_tcp, check_ftp, check_imap, check_jabber, check_nntp,
check_nntps, check_pop, check_simap, check_spop, check_ssmtp, check_udp
and check_clamd support for Nagios/Icinga.

%package time
Summary: Nagios/Icinga Plugin - check_time
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-time
Obsoletes: nagios-plugins-time

%description time
Provides check_time support for Nagios/Icinga.

%package ups
Summary: Nagios/Icinga Plugin - check_ups
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-ups
Obsoletes: nagios-plugins-ups

%description ups
Provides check_ups support for Nagios/Icinga.

%package users
Summary: Nagios/Icinga Plugin - check_users
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-users
Obsoletes: nagios-plugins-users

%description users
Provides check_users support for Nagios/Icinga.

%package wave
Summary: Nagios/Icinga Plugin - check_wave
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Conflicts: nagios-plugins-wave
Obsoletes: nagios-plugins-wave

%description wave
Provides check_wave support for Nagios/Icinga.

%prep
%setup -q

%build
%configure \
	--libexecdir=%{_libdir}/nagios/plugins \
	--with-dbi \
	--with-mysql \
	PATH_TO_QSTAT=%{_bindir}/quakestat \
	PATH_TO_FPING=%{_sbindir}/fping \
	PATH_TO_NTPQ=%{_sbindir}/ntpq \
	PATH_TO_NTPDC=%{_sbindir}/ntpdc \
	PATH_TO_NTPDATE=%{_sbindir}/ntpdate \
	PATH_TO_RPCINFO=%{_sbindir}/rpcinfo \
	--with-ps-command="`which ps` -eo 's uid pid ppid vsz rss pcpu etime comm args'" \
	--with-ps-format='%s %d %d %d %d %d %f %s %s %n' \
	--with-ps-cols=10 \
	--enable-extra-opts \
	--with-ps-varlist='procstat,&procuid,&procpid,&procppid,&procvsz,&procrss,&procpcpu,procetime,procprog,&pos'

make %{?_smp_mflags}
cd plugins
make check_ide_smart
make check_ldap
%if 0%{?fedora}
make check_radius
%endif
make check_pgsql

cd ..


cp %{SOURCE1} ./README.Fedora

%install
sed -i 's,^MKINSTALLDIRS.*,MKINSTALLDIRS = ../mkinstalldirs,' po/Makefile
make AM_INSTALL_PROGRAM_FLAGS="" DESTDIR=%{buildroot} install
install -m 0755 plugins-root/check_icmp %{buildroot}/%{_libdir}/nagios/plugins
install -m 0755 plugins-root/check_dhcp %{buildroot}/%{_libdir}/nagios/plugins
install -m 0755 plugins/check_ide_smart %{buildroot}/%{_libdir}/nagios/plugins
install -m 0755 plugins/check_ldap %{buildroot}/%{_libdir}/nagios/plugins
%if 0%{?fedora}
install -m 0755 plugins/check_radius %{buildroot}/%{_libdir}/nagios/plugins
%endif
install -m 0755 plugins/check_pgsql %{buildroot}/%{_libdir}/nagios/plugins

%ifarch ppc ppc64 ppc64p7 sparc sparc64
rm -f %{buildroot}/%{_libdir}/nagios/plugins/check_sensors
%endif

chmod 644 %{buildroot}/%{_libdir}/nagios/plugins/utils.pm

%find_lang %{name}

%files -f %{name}.lang
%doc ACKNOWLEDGEMENTS AUTHORS ChangeLog CODING COPYING FAQ LEGAL NEWS README REQUIREMENTS SUPPORT THANKS README.Fedora
%{_libdir}/nagios/plugins/negate
%{_libdir}/nagios/plugins/urlize
%{_libdir}/nagios/plugins/utils.sh

%files all

%files apt
%{_libdir}/nagios/plugins/check_apt

%files breeze
%{_libdir}/nagios/plugins/check_breeze

%files by_ssh
%{_libdir}/nagios/plugins/check_by_ssh

%files cluster
%{_libdir}/nagios/plugins/check_cluster

%files dbi
%{_libdir}/nagios/plugins/check_dbi

%files dhcp
%{_libdir}/nagios/plugins/check_dhcp

%files dig
%{_libdir}/nagios/plugins/check_dig

%files disk
%{_libdir}/nagios/plugins/check_disk

%files disk_smb
%{_libdir}/nagios/plugins/check_disk_smb

%files dns
%{_libdir}/nagios/plugins/check_dns

%files dummy
%{_libdir}/nagios/plugins/check_dummy

%files file_age
%{_libdir}/nagios/plugins/check_file_age

%files flexlm
%{_libdir}/nagios/plugins/check_flexlm

%files fping
%{_libdir}/nagios/plugins/check_fping

%files game
%{_libdir}/nagios/plugins/check_game

%files hpjd
%{_libdir}/nagios/plugins/check_hpjd

%files http
%{_libdir}/nagios/plugins/check_http

%files icmp
%{_libdir}/nagios/plugins/check_icmp

%files ifoperstatus
%{_libdir}/nagios/plugins/check_ifoperstatus

%files ifstatus
%{_libdir}/nagios/plugins/check_ifstatus

%files ide_smart
# TODO: % defattr(4750,root,nagios,-)
%{_libdir}/nagios/plugins/check_ide_smart

%files ircd
%{_libdir}/nagios/plugins/check_ircd

%files ldap
%{_libdir}/nagios/plugins/check_ldap
%{_libdir}/nagios/plugins/check_ldaps

%files load
%{_libdir}/nagios/plugins/check_load

%files log
%{_libdir}/nagios/plugins/check_log

%files mailq
%{_libdir}/nagios/plugins/check_mailq

%files mrtg
%{_libdir}/nagios/plugins/check_mrtg

%files mrtgtraf
%{_libdir}/nagios/plugins/check_mrtgtraf

%files mysql
%{_libdir}/nagios/plugins/check_mysql
%{_libdir}/nagios/plugins/check_mysql_query

%files nagios
%{_libdir}/nagios/plugins/check_nagios

%files nt
%{_libdir}/nagios/plugins/check_nt

%files ntp
%{_libdir}/nagios/plugins/check_ntp
%{_libdir}/nagios/plugins/check_ntp_peer
%{_libdir}/nagios/plugins/check_ntp_time

%files nwstat
%{_libdir}/nagios/plugins/check_nwstat

%files oracle
%{_libdir}/nagios/plugins/check_oracle

%files overcr
%{_libdir}/nagios/plugins/check_overcr

%files perl
%{_libdir}/nagios/plugins/utils.pm

%files pgsql
%{_libdir}/nagios/plugins/check_pgsql

%files ping
%{_libdir}/nagios/plugins/check_ping

%files procs
%{_libdir}/nagios/plugins/check_procs

%if 0%{?fedora}
%files radius
%{_libdir}/nagios/plugins/check_radius
%endif

%files real
%{_libdir}/nagios/plugins/check_real

%files rpc
%{_libdir}/nagios/plugins/check_rpc

%ifnarch ppc ppc64 ppc64p7 sparc sparc64
%files sensors
%{_libdir}/nagios/plugins/check_sensors
%endif

%files smtp
%{_libdir}/nagios/plugins/check_smtp

%files snmp
%{_libdir}/nagios/plugins/check_snmp

%files ssh
%{_libdir}/nagios/plugins/check_ssh

%files swap
%{_libdir}/nagios/plugins/check_swap

%files tcp
%{_libdir}/nagios/plugins/check_clamd
%{_libdir}/nagios/plugins/check_ftp
%{_libdir}/nagios/plugins/check_imap
%{_libdir}/nagios/plugins/check_jabber
%{_libdir}/nagios/plugins/check_nntp
%{_libdir}/nagios/plugins/check_nntps
%{_libdir}/nagios/plugins/check_pop
%{_libdir}/nagios/plugins/check_simap
%{_libdir}/nagios/plugins/check_spop
%{_libdir}/nagios/plugins/check_ssmtp
%{_libdir}/nagios/plugins/check_tcp
%{_libdir}/nagios/plugins/check_udp

%files time
%{_libdir}/nagios/plugins/check_time

%files ups
%{_libdir}/nagios/plugins/check_ups

%files users
%{_libdir}/nagios/plugins/check_users

%files wave
%{_libdir}/nagios/plugins/check_wave

%changelog
* Thu Sep 15 2016 Markus Frosch <markus.frosch@netways.de> 2.1.2-1
- Refit SPEC for monitoring-plugins
- Upstream 2.1.2
- Build radius only on Fedora
- Remove ntp-perl, uptime
- Remove setuid and use setcap for dhcp, fping, icmp

* Thu Feb 04 2016 Scott Wilkerson <swilkerson@nagios.com> 2.1.1-1
- Updated to 2.1.1
- Fixes bug #1191896

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Scott Wilkerson <swilkerson@nagios.com> 2.0.3-3
- Fix issue where check_mysql was looking in wrong place for my.cnf
- Fixes bug #1256731

* Thu Aug 27 2015 Kevin Fenzi <kevin@scrye.com> 2.0.3-2
- Add obsoletes for nagios-plugin-linux_raid < 1.4.3-11
- Fixes bug #1256682

* Tue Aug 04 2015 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 1 2014 Sam Kottler <skottler@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1
- Moved SSD-specific patch which landed upstream
- Update patch to binary paths in plugins-scripts/check_log.sh so it applies
- Add -uptime subpackage

* Thu Oct 24 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.5-2
- New check_dbi plugin (BR: libdbi-devel; subpackage: nagios-plugins-dbi)

* Wed Oct 23 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.5-1
- Update to version 1.5
- New project homepage and source download locations
- Disabled patches 1, 6, 8, and 9.
- No linux_raid subpackage (the contrib directory was removed)

* Wed Oct 16 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.4.16-10
- Remove EL4 and EL5 support
- Backport patches to fix check_linux_raid in case of resyncing (rhbz #504721)
- Fix smart attribute comparison (rhbz #913085)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.4.16-8
- Perl 5.18 rebuild

* Wed May 22 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-7
- Build package with PIE flags (#965536)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 17 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-5
- Fix the use lib statement and the external ntp commands paths in check-ntp.pl
  (nagios-plugins-0008-ntpdate-and-ntpq-paths.patch).

* Thu Aug 16 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-4
- Remove the erroneous requirements of nagios-plugins-ntp (#848830)
- Ship check-ntp.pl in the new nagios-plugins-ntp-perl subpackage (#848830)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  9 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-2
- Provides bundled(gnulib) (#821779)

* Mon Jul  9 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-1
- Update to version 1.4.16
- Dropped nagios-plugins-0005-Patch-for-check_linux_raid-with-on-linear-raid0-arra.patch
  (upstream).

* Tue Jun 26 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.15-7
- glibc 2.16 no longer defines gets for ISO C11, ISO C++11, and _GNU_SOURCE
  (#835621): nagios-plugins-0007-undef-gets-and-glibc-2.16.patch

* Tue Jun 26 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.15-6
- The nagios-plugins RPM no longer needs to own the /usr/lib{,64}/nagios/plugins
  directory; this directory is now owned by nagios-common (#835621)
- Small updates (clarification) to the file nagios-plugins.README.Fedora

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.4.15-4
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct  7 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.15-2
- Dropped check_udp sub-package (see rhbz #634067). Anyway it
  provided just a symlink to check_tcp.
- Fixed weird issue with check_swap returning ok in case of
  missing swap (see rhbz #512559).

* Wed Aug 18 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.15-1
- Ver. 1.4.15
- Dropped patch for restoration of behaviour in case of ssl checks

* Tue May 18 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.14-4
- Restore ssl behaviour for check_http in case of self-signed
  certificates (see rhbz #584227).

* Sat Apr 24 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.14-3
- Removed Requires - nagios (see rhbz #469530).
- Added "Requires,Requires(pre): group(nagios)" where necessary
- Sorted %%files sections
- No need to ship INSTALL file
- Added more doc files to main package

* Mon Apr 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.14-2
- Added missing Requires - nagios (see rhbz #469530).
- Fixed path to qstat -> quakestat (see rhbz #533777)
- Disable radius plugin for EL4 - there is not radiuscleint-ng for EL-4

* Wed Mar 10 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.14-1
- Ver. 1.4.14
- Rebased patches.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.4.13-17
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Mike McGrath <mmcgrath@redhat.com> - 1.4.13-15
- Added patch from upstream to fix ntp faults (bz #479030)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Caolán McNamara <caolanm@redhat.com> 1.4.13-13
- rebuild for dependencies

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 1.4.13-12
- rebuild with new openssl

* Mon Oct 20 2008 Robert M. Albrecht <romal@gmx.de> 1.4.13-11
- Enabled --with-extra-opts again

* Mon Oct 20 2008 Robert M. Albrecht <romal@gmx.de> 1.4.13-10
- removed provides perl plugins Bugzilla 457404

* Thu Oct 16 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-9
- This is a "CVS is horrible" rebuild

* Thu Oct  9 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-8
- Rebuilt with a proper patch

* Wed Oct  8 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-7
- Added changed recent permission changes to allow nagios group to execute

* Wed Oct  8 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-6
- Fixed up some permission issues

* Mon Oct  6 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-5
- Fixing patch, missing semicolon

* Sun Sep 28 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-4
- Upstream released new version #464419
- Added patch fix for check_linux_raid #253898
- Upstream releases fix for #451015 - check_ntp_peers
- Upstream released fix for #459309 - check_ntp
- Added Provides Nagios::Plugins for #457404
- Fixed configure line for #458985 check_procs

* Thu Jul 10 2008 Robert M. Albrecht <romal@gmx.de> 1.4.12-3
- Removed --with-extra-opts, does not build in Koji

* Mon Jun 30 2008 Robert M. Albrecht <romal@gmx.de> 1.4.12-2
- Enabled --with-extra-opts

* Sun Jun 29 2008 Robert M. Albrecht <romal@gmx.de> 1.4.12-1
- Upstream released version 1.4.12
- Removed patches ping_timeout.patch and pgsql-fix.patch

* Wed Apr 30 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.11-4
- added patch for check_pgsql

* Wed Apr 09 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.11-2
- Fix for 250588

* Thu Feb 28 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.11-1
- Upstream released version 1.4.11
- Added check_ntp peer and time

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.10-6
- Autorebuild for GCC 4.3

* Tue Feb 12 2008 Mike McGrath <mmcgrath@redhat.com> 1.4-10-5
- Rebuild for gcc43

* Thu Jan 10 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.10-4
- Fixed check_log plugin #395601

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.4.10-2
- Rebuild for deps

* Thu Dec 06 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.10-1
- Upstream released new version
- Removed some patches

* Fri Oct 26 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-9
- Fix for Bug 348731 and CVE-2007-5623

* Wed Aug 22 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-7
- Rebuild for BuildID
- License change

* Fri Aug 10 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-6
- Fix for check_linux_raid - #234416
- Fix for check_ide_disk - #251635

* Tue Aug 07 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-2
- Fix for check_smtp - #251049

* Fri Apr 13 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-1
- Upstream released new version

* Fri Feb 23 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.6-1
- Upstream released new version

* Sun Dec 17 2006 Mike McGrath <imlinux@gmail.com> 1.4.5-1
- Upstream released new version

* Fri Oct 27 2006 Mike McGrath <imlinux@gmail.com> 1.4.4-2
- Enabled check_smart_ide
- Added patch for linux_raid
- Fixed permissions on check_icmp

* Tue Oct 24 2006 Mike McGrath <imlinux@gmail.com> 1.4.4-1
- Upstream new version
- Disabled check_ide_smart (does not compile cleanly/too lazy to fix right now)
- Added check_apt

* Sun Aug 27 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-18
- Removed utils.pm from the base nagios-plugins package into its own package

* Tue Aug 15 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-17
- Added requires qstat for check_game

* Thu Aug 03 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-16
- Providing path to qstat

* Thu Aug 03 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-15
- Fixed permissions on check_dhcp
- Added check_game
- Added check_radius
- Added patch for ntp

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-14
- Patched upstream issue: 196356

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-13
- nagios-plugins-all now includes nagios-plugins-mysql

* Thu Jun 22 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-12
- removed sensors support for sparc and sparc64

* Thu Jun 22 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-11
- Created a README.Fedora explaining how to install other plugins

* Sun Jun 11 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-9
- Removed check_sensors in install section

* Sat Jun 10 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-8
- Inserted conditional blocks for ppc exception.

* Wed Jun 07 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-7
- Removed sensors from all plugins and added excludearch: ppc

* Tue Jun 06 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-6
- For ntp plugins requires s/ntpc/ntpdc/

* Sat Jun 03 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-5
- Fixed a few syntax errors and removed an empty export

* Fri May 19 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-4
- Now using configure macro instead of ./configure
- Added BuildRequest: perl(Net::SNMP)
- For reference, this was bugzilla.redhat.com ticket# 176374

* Fri May 19 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-3
- Added check_ide_smart
- Added some dependencies
- Added support for check_if* (perl-Net-SNMP now in extras)
- nagios-plugins now owns dir %%{_libdir}/nagios

* Sat May 13 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-2
- Added a number of requires that don't get auto-detected

* Sun May 07 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-1
- Upstream remeased 1.4.3

* Tue Apr 18 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-9
- Fixed a typo where nagios-plugins-all required nagios-plugins-httpd

* Mon Mar 27 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-8
- Updated to CVS head for better MySQL support

* Sun Mar 5 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-7
- Added a nagios-plugins-all package

* Wed Feb 1 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-6
- Added provides for check_tcp

* Mon Jan 30 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-5
- Created individual packages for all check_* scripts

* Tue Dec 20 2005 Mike McGrath <imlinux@gmail.com> 1.4.2-4
- Fedora friendly spec file

* Mon May 23 2005 Sean Finney <seanius@seanius.net> - cvs head
- just include the nagios plugins directory, which will automatically include
  all generated plugins (which keeps the build from failing on systems that
  don't have all build-dependencies for every plugin)

* Thu Mar 04 2004 Karl DeBisschop <karl[AT]debisschop.net> - 1.4.0alpha1
- extensive rewrite to facilitate processing into various distro-compatible specs

* Thu Mar 04 2004 Karl DeBisschop <karl[AT]debisschop.net> - 1.4.0alpha1
- extensive rewrite to facilitate processing into various distro-compatible specs

