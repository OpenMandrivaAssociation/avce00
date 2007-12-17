Name:		avce00
Version:	2.0.0
Release:	%mkrel 1
Summary:	Arc/Info (binary) Vector Coverage <-> E00 Utilities
License:	BSD-like
URL:		http://avce00.maptools.org/
Source:		http://avce00.maptools.org/dl/%{name}-%{version}.tar.gz
Group:		Sciences/Geosciences

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
