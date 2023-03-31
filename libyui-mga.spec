%define major 15
%define libname %mklibname yui %{major}-mga
%define develname %mklibname -d yui-mga

Name:		libyui-mga
Version:	1.2.1
Release:	2
Summary:	UI abstraction library - Mageia extension widget base plugin
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/manatools/libyui-mga
Source0:	https://github.com/manatools/libyui-mga/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	doxygen
#BuildRequires:	texlive
BuildRequires:	ghostscript
BuildRequires:	graphviz
Requires:	libyui

%description
%{summary}.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	libyui
Provides:	%{name} = %{EVRD}
%rename %{_lib}yui-mga8

%description -n %{libname}
This package contains the library needed to run programs
dynamically linked with libyui-mga.

%files -n %{libname}
%{_libdir}/libyui-mga.so.%{major}*

#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	%{summary} header files
Group:		Development/C++
Provides:	%{name}-devel = %{EVRD}
Requires:	%{name} = %{EVRD}

%description -n %{develname}
This package provides headers files for libyui-mga development.

%files -n %{develname}
%{_includedir}/yui
%{_libdir}/libyui-mga.so
%{_libdir}/pkgconfig/libyui-mga.pc
#%%{_libdir}/cmake/libyui-mga
%doc README.md TODO.md ./examples MAINTAINER COPYING.lgpl-2.1 COPYING.lgpl-3

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
#./bootstrap.sh
%cmake \
	-DYPREFIX=%{_prefix} \
	-DDOC_DIR=%{_docdir} \
	-DLIB_DIR=%{_lib}    \
	-DENABLE_DEBUG=1     \
	-DSKIP_LATEX:BOOL=yes \
	-DINSTALL_DOCS=yes   \
	-DBUILD_EXAMPLES=off \
	-DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
	-DWERROR=off \
	-G Ninja

%ninja_build
#%%ninja_build docs

%install
%ninja_install -C build
