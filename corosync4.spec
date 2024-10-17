%define major	4
%define	libconfdb %mklibname libconfdb %{major}
%define	libcoroipcc %mklibname libcoroipcc %{major}
%define	libcoroipcs %mklibname libcoroipcs %{major}
%define	libevs %mklibname libevs %{major}
%define	liblogsys %mklibname liblogsys %{major}
%define	libpload %mklibname libpload %{major}
%define	libcpg		%mklibname cpg %{major}
%define	libsam		%mklibname sam %{major}
%define	libcfg		%mklibname cfg %{major}
%define	libquorum	%mklibname quorum %{major}
%define	libtotem_pg	%mklibname totem_pg %{major}
%define	libvotequorum	%mklibname votequorum %{major}
%define devname %mklibname -d corosync %{major}

Summary:	The Corosync Cluster Engine and Application Programming Interfaces
Name:		corosync
Version:	1.2.8
Release:	14
License:	BSD
Group:		System/Base
Url:		https://www.corosync.org
Source0:	ftp://ftp:downloads@ftp.corosync.org/downloads/corosync-%{version}/corosync-%{version}.tar.gz

BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(libqb)
Requires(post,preun):	rpm-helper

%description 
This package contains the Corosync Cluster Engine Executive, several default
APIs and libraries, default configuration files, and an init script.

%package	-n %{libconfdb}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Obsoletes:	%{_lib}corosync4 1.2.8-5

%description	-n %{libconfdb}
This package contains corosync libraries.

%package	-n %{libcoroipcc}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libcoroipcc}
This package contains corosync libraries.

%package	-n %{libcoroipcs}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libcoroipcs}
This package contains corosync libraries.

%package	-n %{libevs}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libevs}
This package contains corosync libraries.

%package	-n %{liblogsys}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{liblogsys}
This package contains corosync libraries.

%package	-n %{libpload}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libpload}
This package contains corosync libraries.

%package	-n %{libcpg}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libcpg}
This package contains corosync libraries.

%package	-n %{libsam}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libsam}
This package contains corosync libraries.

%package	-n %{libcfg}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libcfg}
This package contains corosync libraries.

%package	-n %{libquorum}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libquorum}
This package contains corosync libraries.

%package	-n %{libtotem_pg}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libtotem_pg}
This package contains corosync libraries.

%package	-n %{libvotequorum}
Summary:	The Corosync Cluster Engine Libraries
Group:		System/Libraries
Conflicts:	%{_lib}corosync4 1.2.8-5

%description	-n %{libvotequorum}
This package contains corosync libraries.

%package	-n %{devname}
Summary:	The Corosync Cluster Engine Development Kit
Group:		Development/C
Requires:	%{libconfdb} = %{version}-%{release}
Requires:	%{libcoroipcc} = %{version}-%{release}
Requires:	%{libcoroipcs} = %{version}-%{release}
Requires:	%{libevs} = %{version}-%{release}
Requires:	%{liblogsys} = %{version}-%{release}
Requires:	%{libpload} = %{version}-%{release}
Requires:	%{libcpg} = %{version}-%{release}
Requires:	%{libsam} = %{version}-%{release}
Requires:	%{libcfg} = %{version}-%{release}
Requires:	%{libquorum} = %{version}-%{release}
Requires:	%{libtotem_pg} = %{version}-%{release}
Requires:	%{libvotequorum} = %{version}-%{release}
Provides:	%{name}-devel = %{version}

%description	-n %{devname}
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%prep
%setup -q

%configure2_5x \
	--with-lcrso-dir=%{_libexecdir}/lcrso

%build
%make

%install
%makeinstall_std
install -d %{buildroot}%{_initddir}
mv %{buildroot}/etc/init.d/* %{buildroot}/%{_initddir}

## tree fixup
# drop static libs
rm -f %{buildroot}%{_libdir}/*.a
# drop docs and html docs for now
rm -rf %{buildroot}%{_docdir}/*

#add logs directory
install -d %{buildroot}/var/log/%{name}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%postun
[ "$1" -ge "1" ] && /sbin/service corosync condrestart &>/dev/null || :

%files 
%doc LICENSE SECURITY
%{_initddir}/corosync
%dir %{_libexecdir}/lcrso
%{_libexecdir}/lcrso/*.lcrso
%{_sbindir}/corosync*
%dir %{_sysconfdir}/corosync
%dir %{_sysconfdir}/corosync/service.d
%dir %{_sysconfdir}/corosync/uidgid.d
%config(noreplace) %{_sysconfdir}/corosync/corosync.conf.example
%dir %{_localstatedir}/lib/corosync
%{_mandir}/man8/corosync_overview.8*
%{_mandir}/man8/confdb_overview.8*
%{_mandir}/man8/coroipc_overview.8*
%{_mandir}/man8/evs_overview.8*
%{_mandir}/man8/logsys_overview.8*
%{_mandir}/man8/corosync-*.8*
%{_mandir}/man8/corosync.8*
%{_mandir}/man5/corosync.conf.5*
%dir /var/log/%{name}

%files -n %{libconfdb}
%{_libdir}/libconfdb.so.%{major}*

%files -n %{libcoroipcc}
%{_libdir}/libcoroipcc.so.%{major}*

%files -n %{libcoroipcs}
%{_libdir}/libcoroipcs.so.%{major}*

%files -n %{libevs}
%{_libdir}/libevs.so.%{major}*

%files -n %{liblogsys}
%{_libdir}/liblogsys.so.%{major}*

%files -n %{libpload}
%{_libdir}/libpload.so.%{major}*

%files -n %{libcpg}
%{_libdir}/libcpg.so.%{major}*

%files -n %{libsam}
%{_libdir}/libsam.so.%{major}*

%files -n %{libcfg}
%{_libdir}/libcfg.so.%{major}*

%files -n %{libquorum}
%{_libdir}/libquorum.so.%{major}*

%files -n %{libtotem_pg}
%{_libdir}/libtotem_pg.so.%{major}*

%files -n %{libvotequorum}
%{_libdir}/libvotequorum.so.%{major}*

%files -n %{devname}
%doc LICENSE README.recovery
%{_includedir}/corosync/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*
%{_mandir}/man8/cpg_overview.8*
%{_mandir}/man8/votequorum_overview.8*
%{_mandir}/man8/sam_overview.8*
