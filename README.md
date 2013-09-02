rpm-sparkey
===========

An RPM spec file to build and install the sparkey key/value storage library.

To build:

You will need the versions of automake, autoconf and libtool from http://repo.milford.io

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`sudo yum -y install gcc44 snappy-devel libtool automake autoconf doxygen`

`wget https://raw.github.com/nmilford/rpm-sparkey/master/sparkey.spec -O ~/rpmbuild/SPECS/sparkey.spec`

`wget https://codeload.github.com/spotify/sparkey/zip/master -O ~/rpmbuild/SOURCES/sparkey.zip`

`QA_RPATHS=$[ 0x0001 ]  rpmbuild -bb ~/rpmbuild/SPECS/sparkey.spec`