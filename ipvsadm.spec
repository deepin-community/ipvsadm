%define prefix   /usr

Summary: Utility to administer the Linux Virtual Server
Name: ipvsadm
Version: 1.31
Release: 1
License: GPL
URL: http://www.LinuxVirtualServer.org/
Group: Applications/System
Source0: http://www.LinuxVirtualServer.org/software/ipvsadm-%{version}.tar.gz
BuildRoot: /var/tmp/%name-%{PACKAGE_VERSION}-root
Provides: %{name}-%{version}
Conflicts: piranha <= 0.4.14

%description
ipvsadm is a utility to administer the IP Virtual Server services
offered by the latest Linux kernel 2.6.x.


%prep
%setup -n %{name}-%{version}


%build
CFLAGS="${RPM_OPT_FLAGS}" make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/{sbin,%{_mandir}/man8,etc/rc.d/init.d}
make install BUILD_ROOT=${RPM_BUILD_ROOT} MANDIR=%{_mandir}


%files
%defattr(-,root,root)
%doc README
%config /etc/rc.d/init.d/ipvsadm
/sbin/ipvsadm*
%{_mandir}/man8/ipvsadm*

%post
/sbin/chkconfig --add ipvsadm

%preun
/sbin/chkconfig --del ipvsadm


%clean
rm -rf $RPM_BUILD_DIR/%{name}
rm -rf $RPM_BUILD_ROOT


%changelog
* Thu Jun 23 2005 Steve Nielsen <snielsen@comscore.com>
- Respect rpmmacros that might be set (by using rpm --eval)

* Sat Dec 20 2003 Wensong Zhang <wensong@linux-vs.org>
- tidy up the description

* Sat Apr  5 2003 Wensong Zhang <wensong@linux-vs.org>
- Removed the unnecessary Docdir setting.

* Thu Dec 16 2001 Wensong Zhang <wensong@linuxvirtualserver.org>
- Changed to install ipvsadm man pages according to the %{_mandir}

* Thu Dec 30 2000 Wensong Zhang <wensong@linuxvirtualserver.org>
- update the %file section

* Thu Dec 17 2000 Wensong Zhang <wensong@linuxvirtualserver.org>
- Added a if-condition to keep both new or old rpm utility building
  the package happily.

* Tue Dec 12 2000 P.Copeland <bryce@redhat.com>
- Small modifications to make the compiler happy in RH7 and the Alpha
- Fixed the documentation file that got missed off in building
  the rpm
- Made a number of -pedantic mods though popt will not compile with
  -pedantic

* Wed Aug 9 2000 Horms <horms@vergenet.net>
- Removed Obseletes tag as ipvsadm is back in /sbin where it belongs 
  as it is more or less analogous to both route and ipchains both of
  which reside in /sbin.
- Create directory to install init script into. Init scripts won't install
  into build directory unless this is done

* Thu Jul  6 2000 Wensong Zhang <wensong@linuxvirtualserver.org>
- Changed to build rpms on the ipvsadm tar ball directly

* Wed Jun 21 2000 P.Copeland <copeland@redhat.com>
- fixed silly install permission settings

* Mon Jun 19 2000 P.Copeland <copeland@redhat.com>
- Added 'dist' and 'rpms' to the Makefile
- Added Obsoletes tag since there were early versions
  of ipvsadm-*.rpm that installed in /sbin
- Obsolete tag was a bit vicious re: piranha

* Mon Apr 10 2000 Horms <horms@vergenet.net>
- created for version 1.9
