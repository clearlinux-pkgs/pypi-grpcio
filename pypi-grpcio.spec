#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-grpcio
Version  : 1.54.0
Release  : 113
URL      : https://files.pythonhosted.org/packages/ef/e4/5c717f3c6c65b7c5ff2542ca25d6c2ce0f99d9ee9119620c6e2325a6da79/grpcio-1.54.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ef/e4/5c717f3c6c65b7c5ff2542ca25d6c2ce0f99d9ee9119620c6e2325a6da79/grpcio-1.54.0.tar.gz
Summary  : HTTP/2-based RPC framework
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-grpcio-license = %{version}-%{release}
Requires: pypi-grpcio-python = %{version}-%{release}
Requires: pypi-grpcio-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(coverage)
BuildRequires : pypi(cython)
BuildRequires : pypi(protobuf)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython
BuildRequires : python3-dev

%description
===========
        
        |compat_check_pypi|
        
        Package for gRPC Python.

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
Requires: pypi(coverage)
Requires: pypi(cython)
Requires: pypi(protobuf)
Requires: pypi(wheel)

%description python3
python3 components for the pypi-grpcio package.


%prep
%setup -q -n grpcio-1.54.0
cd %{_builddir}/grpcio-1.54.0
pushd ..
cp -a grpcio-1.54.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683038178
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-grpcio
cp %{_builddir}/grpcio-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-grpcio/242ec6abfdd8c114f2e803b84934469c299348fc || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-grpcio/242ec6abfdd8c114f2e803b84934469c299348fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
