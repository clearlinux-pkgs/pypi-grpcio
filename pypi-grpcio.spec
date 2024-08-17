#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v18
# autospec commit: f35655a
#
Name     : pypi-grpcio
Version  : 1.65.5
Release  : 135
URL      : https://files.pythonhosted.org/packages/6c/d8/1d8f1640649808db79b689d65b03556077d5504baad5ea64b167a5adedad/grpcio-1.65.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/6c/d8/1d8f1640649808db79b689d65b03556077d5504baad5ea64b167a5adedad/grpcio-1.65.5.tar.gz
Summary  : HTTP/2-based RPC framework
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-grpcio-license = %{version}-%{release}
Requires: pypi-grpcio-python = %{version}-%{release}
Requires: pypi-grpcio-python3 = %{version}-%{release}
BuildRequires : abseil-cpp-dev
BuildRequires : buildreq-distutils3
BuildRequires : c-ares-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(protobuf)
BuildRequires : pypi-cython
BuildRequires : python3-dev
BuildRequires : re2-dev
BuildRequires : zlib-dev
Patch1: 0001-use-c-17-to-avoid-compiler-errors.patch

%description
# gRPC – An RPC library and framework
gRPC is a modern, open source, high-performance remote procedure call (RPC)
framework that can run anywhere. gRPC enables client and server applications to
communicate transparently, and simplifies the building of connected systems.

%package license
Summary: license components for the pypi-grpcio package.
Group: Default

%description license
license components for the pypi-grpcio package.


%package python
Summary: python components for the pypi-grpcio package.
Group: Default
Requires: pypi-grpcio-python3 = %{version}-%{release}

%description python
python components for the pypi-grpcio package.


%package python3
Summary: python3 components for the pypi-grpcio package.
Group: Default
Requires: python3-core
Provides: pypi(grpcio)

%description python3
python3 components for the pypi-grpcio package.


%prep
%setup -q -n grpcio-1.65.5
cd %{_builddir}/grpcio-1.65.5
%patch -P 1 -p1

%build
## build_prepend content
export GRPC_PYTHON_LDFLAGS="$(pkg-config --libs protobuf)"
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1
export GRPC_PYTHON_BUILD_SYSTEM_RE2=1
export GRPC_PYTHON_BUILD_SYSTEM_ABSL=1
export GRPC_PYTHON_BUILD_WITH_SYSTEMD=1
export GRPC_BUILD_WITH_BORING_SSL_ASM=0
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723871016
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
## install_prepend content
export GRPC_PYTHON_LDFLAGS="$(pkg-config --libs protobuf)"
export GRPC_PYTHON_BUILD_WITH_CYTHON=1
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export GRPC_PYTHON_BUILD_SYSTEM_CARES=1
export GRPC_PYTHON_BUILD_SYSTEM_RE2=1
export GRPC_PYTHON_BUILD_SYSTEM_ABSL=1
export GRPC_PYTHON_BUILD_WITH_SYSTEMD=1
export GRPC_BUILD_WITH_BORING_SSL_ASM=0
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-grpcio
cp %{_builddir}/grpcio-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-grpcio/242ec6abfdd8c114f2e803b84934469c299348fc || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-grpcio/242ec6abfdd8c114f2e803b84934469c299348fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
