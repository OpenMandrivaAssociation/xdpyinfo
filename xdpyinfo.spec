Name:		xdpyinfo
Version:	1.3.4
Release:	1
Summary:	Display information utility for X
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xext) >= 1.0.0
BuildRequires: pkgconfig(xtst) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xxf86dga)
BuildRequires: pkgconfig(xxf86misc)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(dmx)

%description
Xdpyinfo is a utility for displaying information about an X server. It is used
to examine the capabilities of a server, the predefined values for various
parameters used in communicating between clients and the server, and the
different types of screens and visuals that are available.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xdpyinfo
%doc %{_mandir}/man1/xdpyinfo.*
