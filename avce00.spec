Name:		avce00
Version:	2.0.0
Release:	%mkrel 4
Summary:	Arc/Info (binary) Vector Coverage <-> E00 Utilities
License:	BSD-like
URL:		http://avce00.maptools.org/
Source:		http://avce00.maptools.org/dl/%{name}-%{version}.tar.gz
Group:		Sciences/Geosciences
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
AVCE00 is an Open Source (i.e. Free!) ANSI-C library that makes Arc/Info
(binary) Vector Coverages appear as E00! It allows you to read and write binary
coverages just as if they were E00 files.

For those who do not need a library but simply want to convert some coverages,
the package includes the "AVCIMPORT" and "AVCEXPORT" conversion programs.

%package -n %{name}-devel
License:	BSD-like
Group:		Sciences/Geosciences
Summary:	Arc/Info (binary) Vector Coverage <-> E00 Library

%description -n %{name}-devel
AVCE00 is an Open Source (i.e. Free!) ANSI-C library that makes Arc/Info
(binary) Vector Coverages appear as E00! It allows you to read and write binary
coverages just as if they were E00 files.

The C library can be easily plugged into existing E00 translators to add
support for binary coverages simply by replacing your existing translator's
read/write function by the AVCE00ReadNextLine() and AVCE00WriteNextLine()
functions provided by the library. See the library documentation for all the
details.

This package includes the development files (headers and static library)
for developing applications which use the avc library.

%prep
%setup -q


%build
#configure
%make

%install
rm -Rf %{buildroot}
install -d %{buildroot}/{%{_includedir},%{_bindir},%{_libdir}}
install *.h %{buildroot}/%{_includedir}
install *.a %{buildroot}/%{_libdir}
install avc{delete,export,import,test} ex_avcwrite %{buildroot}/%{_bindir}


%files
%defattr(-,root,root)
%{_bindir}/*avc*

%files -n %{name}-devel
%{_includedir}/*.h
%{_libdir}/avc.a


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-4mdv2011.0
+ Revision: 616671
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 2.0.0-3mdv2010.0
+ Revision: 423998
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-2mdv2009.0
+ Revision: 226207
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2.0.0-1mdv2008.1
+ Revision: 135825
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Buchan Milne <bgmilne@mandriva.org> 2.0.0-1mdv2008.0
+ Revision: 68206
- New version 2.0.0
- Add URL
- Import avce00



* Wed Jul 05 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.3.0-3mdv2007.0
- fix group

* Thu Feb 16 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.0-2mdk
- Fix Group (thanks plg)

* Sun Jan 01 2006 Buchan Milne <bgmilne@mandriva.org> 1.3.0-1
- initial Mandriva package
