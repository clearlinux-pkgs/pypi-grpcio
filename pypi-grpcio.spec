#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-grpcio
Version  : 1.43.0
Release  : 82
URL      : https://files.pythonhosted.org/packages/c6/6b/5f7cd38ff3ac80f47cbe56618fe45502f90b41a56f5d9e248ee574e14687/grpcio-1.43.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c6/6b/5f7cd38ff3ac80f47cbe56618fe45502f90b41a56f5d9e248ee574e14687/grpcio-1.43.0.tar.gz
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
BuildRequires : pypi(six)
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
Requires: pypi(six)

%description python3
python3 components for the pypi-grpcio package.


%prep
%setup -q -n grpcio-1.43.0
cd %{_builddir}/grpcio-1.43.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642361206
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-grpcio
cp %{_builddir}/grpcio-1.43.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-grpcio/34ac89724cb7e3fb36bcfe93efabfd012c569a0e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-grpcio/34ac89724cb7e3fb36bcfe93efabfd012c569a0e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
