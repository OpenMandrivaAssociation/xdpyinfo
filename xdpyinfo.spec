Name:		xdpyinfo
Version:	1.3.1
Release:	4
Summary:	Display information utility for X
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xext) >= 1.0.0
BuildRequires: pkgconfig(xtst) >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
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
%setup -q

%build
autoreconf -fi
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xdpyinfo
%{_mandir}/man1/xdpyinfo.*



%changelog
* Sat Oct 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.0-1mdv2012.0
+ Revision: 705661
- update to new version 1.3.0

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2
+ Revision: 671300
- mass rebuild

* Mon Oct 04 2010 Thierry Vignaud <tv@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 582815
- new release

* Mon Nov 16 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-2mdv2010.1
+ Revision: 466663
- Add libxp-devel to BuildRequires

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 464806
- Fix BuildRequires (some of them are not strictly needed, but reduce package
  functionality)
- New version: 1.1.0

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.3-3mdv2009.1
+ Revision: 351201
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2009.0
+ Revision: 266080
- rebuild early 2009.0 package (before pixel changes)

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.0.3-1mdv2009.0
+ Revision: 211776
- New version

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 155914
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 76437
- rebuild for 2008
- slight spec clean
- new release 1.0.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:34:52 (31402)
- fill in more missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

