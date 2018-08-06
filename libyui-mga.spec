%define         major        8
%define         libname      %mklibname yui-mga %{major}
%define         develname    %mklibname -d yui-mga

Name:           libyui-mga
Version:        1.0.8
Release:        1
Summary:        UI abstraction library - Mageia extension widget base plugin
License:        LGPLv2+
Group:          System/Libraries
Url:            https://github.com/manatools/libyui-mga
Source0:        https://github.com/manatools/libyui-mga/archive/%{version}.tar.gz

BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	texlive
BuildRequires:	ghostscript
BuildRequires:	graphviz
Requires:	libyui

%description
%{summary}

#-----------------------------------------------------------------------

%package -n %libname
Summary:        %{summary}
Group:          System/Libraries
Requires:       libyui
Provides:       %{name} = %{version}-%{release}

%description -n %libname
This package contains the library needed to run programs
dynamically linked with libyui-mga.

%files -n %libname
%doc COPYING*
%{_libdir}/libyui-mga.so.*


#-----------------------------------------------------------------------

%package -n %develname
Summary:        %{summary} header files
Group:          Development/C++
Requires:       libyui-devel
Requires:       %{name} = %{version}-%{release}


%description -n %develname
This package provides headers files for libyui-mga development.

%files -n %develname
%{_includedir}/yui
%{_libdir}/libyui-mga.so
%{_libdir}/pkgconfig/libyui-mga.pc
%{_libdir}/cmake/libyui-mga
%doc %{_docdir}/libyui-mga%{major}

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
./bootstrap.sh
%cmake \
	-DYPREFIX=%{_prefix} \
	-DDOC_DIR=%{_docdir} \
	-DLIB_DIR=%{_lib}    \
	-DENABLE_DEBUG=1     \
	-DENABLE_WERROR:BOOL=OFF \
	-DSKIP_LATEX:BOOL=yes \
	-DINSTALL_DOCS=yes   \
	-DENABLE_EXAMPLES=no \
	-DCMAKE_BUILD_TYPE=RELWITHDEBINFO

%make_build
%make_build docs

%install
%make_install -C build
