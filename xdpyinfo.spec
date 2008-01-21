Name:		xdpyinfo
Version:	1.0.2
Release:	%mkrel 2
Summary:	Display information utility for X
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libx11-devel		>= 1.1.3
BuildRequires:	libxext-devel		>= 1.0.3
BuildRequires:	libxtst-devel		>= 1.0.3
BuildRequires:	libxrender-devel	>= 0.9.4

%description
Xdpyinfo is a utility for displaying information about an X server. It is used
to examine the capabilities of a server, the predefined values for various
parameters used in communicating between clients and the server, and the
different types of screens and visuals that are available.

%prep
%setup -q

%build
%configure	--x-includes=%{_includedir}\
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

