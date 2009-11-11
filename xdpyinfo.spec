Name:		xdpyinfo
Version:	1.1.0
Release:	%mkrel 1
Summary:	Display information utility for X
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxtst-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libxxf86vm-devel
BuildRequires: libxxf86dga-devel
BuildRequires: libxxf86misc-devel
BuildRequires: libxi-devel
BuildRequires: libxrender-devel
BuildRequires: libxcomposite-devel
BuildRequires: libxinerama-devel
BuildRequires: libdmx-devel

%description
Xdpyinfo is a utility for displaying information about an X server. It is used
to examine the capabilities of a server, the predefined values for various
parameters used in communicating between clients and the server, and the
different types of screens and visuals that are available.

%prep
%setup -q

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xdpyinfo
%{_mandir}/man1/xdpyinfo.*

