# To build:
#
# You will need the versions of automake, autoconf and libtool from http://repo.milford.io
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
# sudo yum -y install gcc44 snappy-devel libtool automake autoconf doxygen
#
# wget https://raw.github.com/nmilford/rpm-sparkey/master/sparkey.spec -O ~/rpmbuild/SPECS/sparkey.spec
# wget https://codeload.github.com/spotify/sparkey/zip/master -O ~/rpmbuild/SOURCES/sparkey.zip
#
# QA_RPATHS=$[ 0x0001 ]  rpmbuild -bb ~/rpmbuild/SPECS/sparkey.spec

Name:      sparkey
Version:   0.0.1
Release:   1
Summary:   A simple constant key/value storage library.
License:   Apache 2.0
URL:       https://github.com/spotify/sparkey
Group:     Development/Libraries
Source0:   sparkey.zip
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Packager:  Nathan Milford <nathan@milford.io>
BuildRequires: doxygen
BuildRequires: autoconf >= 2.69
BuildRequires: automake >= 1.14
BuildRequires: libtool >= 2.4
BuildRequires: snappy-devel
BuildRequires: gcc44
Requires: snappy

%description
Sparkey is a simple constant key/value storage library. It is mostly suited for
read heavy systems with infrequent large bulk inserts. It includes both a C 
library for working with sparkey index and log files (libsparkey), and a
command line utility for getting info about and reading values from a sparkey
index/log (sparkey).

%package devel
Summary:  A simple constant key/value storage library.
Group:    Development/Libraries
Requires: %{name}= %{version}-%{release}

%description devel
Contains developmental libraries for sparkey.

%prep

%setup -n sparkey-master
%build
export CC=gcc44
autoreconf --install
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR="%{buildroot}"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/*
%{_docdir}/%{name}/*

%files devel
%defattr(-,root,root)
%{_libdir}/*
%{_includedir}/%{name}/*.h

%changelog
* Mon Sep 02 2013 Nathan Milford <nathan@milford.io> 1.14-1
- First shot.