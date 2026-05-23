%bcond clang 1

# TDE variables
%define tde_pkg ktechlab
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Circuit simulator for microcontrollers and electronics [Trinity]
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/development/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_ALL=ON -DWITH_ALL_OPTIONS=ON -DWITH_GPSIM=OFF
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
KTechlab is a circuit simulator with a nice, clickable and discoverable
interface. It supports many discrete components, logic circuits as well
as PIC programming in its own Basic dialect and some form of assembler. 

Homepage: http://ktechlab.org/


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_prefix}/bin/ktechlab
%{tde_prefix}/bin/microbe
%{tde_prefix}/share/applications/tde/ktechlab.desktop
%{tde_prefix}/share/apps/katepart/syntax/microbe.xml
%{tde_prefix}/share/apps/ktechlab
%{tde_prefix}/share/config.kcfg/ktechlab.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/ktechlab/
%{tde_prefix}/share/icons/hicolor/*/*/*.png
%{tde_prefix}/share/mimelnk/application/x-circuit.desktop
%{tde_prefix}/share/mimelnk/application/x-flowcode.desktop
%{tde_prefix}/share/mimelnk/application/x-ktechlab.desktop
%{tde_prefix}/share/mimelnk/application/x-microbe.desktop
%{tde_prefix}/share/man/man1/ktechlab.1*
%{tde_prefix}/share/man/man1/microbe.1*

