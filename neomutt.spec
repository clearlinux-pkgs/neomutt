#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : neomutt
Version  : 20200814
Release  : 5
URL      : https://github.com/neomutt/neomutt/archive/20200814.tar.gz
Source0  : https://github.com/neomutt/neomutt/archive/20200814.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 Unlicense
Requires: neomutt-bin = %{version}-%{release}
Requires: neomutt-libexec = %{version}-%{release}
Requires: neomutt-license = %{version}-%{release}
Requires: neomutt-locales = %{version}-%{release}
Requires: neomutt-man = %{version}-%{release}
BuildRequires : cyrus-sasl-dev
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : gnutls-dev
BuildRequires : krb5-dev
BuildRequires : libidn-dev
BuildRequires : libxml2
BuildRequires : libxslt
BuildRequires : lmdb-dev
BuildRequires : ncurses-dev
BuildRequires : notmuch-dev
Patch1: 0001-Disable-error-on-invalid-configure-item.patch

%description
# This is the NeoMutt Project
[![Stars](https://img.shields.io/github/stars/neomutt/neomutt.svg?style=social&label=Stars)](https://github.com/neomutt/neomutt "Give us a Star")
[![Twitter](https://img.shields.io/twitter/follow/NeoMutt_Org.svg?style=social&label=Follow)](https://twitter.com/NeoMutt_Org "Follow us on Twitter")
[![Contributors](https://img.shields.io/badge/Contributors-189-orange.svg)](https://github.com/neomutt/neomutt/blob/master/AUTHORS.md "All of NeoMutt's Contributors")
[![Release](https://img.shields.io/github/release/neomutt/neomutt.svg)](https://github.com/neomutt/neomutt/releases/latest "Latest Release Notes")
[![Code build](https://img.shields.io/travis/com/neomutt/neomutt/master?label=code)](https://travis-ci.com/neomutt/neomutt "Latest Automatic Code Build")
[![Coverity Scan](https://img.shields.io/coverity/scan/8495.svg)](https://scan.coverity.com/projects/neomutt-neomutt "Latest Code Static Analysis")
[![Website build](https://img.shields.io/travis/neomutt/neomutt.github.io.svg?label=website)](https://travis-ci.com/neomutt/neomutt.github.io "Latest Website Test")

%package bin
Summary: bin components for the neomutt package.
Group: Binaries
Requires: neomutt-libexec = %{version}-%{release}
Requires: neomutt-license = %{version}-%{release}

%description bin
bin components for the neomutt package.


%package doc
Summary: doc components for the neomutt package.
Group: Documentation
Requires: neomutt-man = %{version}-%{release}

%description doc
doc components for the neomutt package.


%package libexec
Summary: libexec components for the neomutt package.
Group: Default
Requires: neomutt-license = %{version}-%{release}

%description libexec
libexec components for the neomutt package.


%package license
Summary: license components for the neomutt package.
Group: Default

%description license
license components for the neomutt package.


%package locales
Summary: locales components for the neomutt package.
Group: Default

%description locales
locales components for the neomutt package.


%package man
Summary: man components for the neomutt package.
Group: Default

%description man
man components for the neomutt package.


%prep
%setup -q -n neomutt-20200814
cd %{_builddir}/neomutt-20200814
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597436780
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-mailpath=/var/spool/mail/ \
--enable-imap \
--enable-pop \
--enable-smtp \
--with-gnutls=yes \
--with-gss=yes \
--with-notmuch=yes \
--with-sasl=yes \
--enable-sidebar \
--enable-hcache \
--enable-debug \
--with-lmdb=yes
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1597436780
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/neomutt
cp %{_builddir}/neomutt-20200814/LICENSE.md %{buildroot}/usr/share/package-licenses/neomutt/b11b797fa13b0935d0e0b13a84f7dd413f9d6ab3
cp %{_builddir}/neomutt-20200814/autosetup/LICENSE %{buildroot}/usr/share/package-licenses/neomutt/34b2f1d7acba3eeb992e4281307640989cd08d0a
cp %{_builddir}/neomutt-20200814/contrib/keybase/LICENSE %{buildroot}/usr/share/package-licenses/neomutt/24944bf7920108f5a4790e6071c32e9102760c37
%make_install
%find_lang neomutt

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/neomutt

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/neomutt/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/neomutt/pgpewrap
/usr/libexec/neomutt/smime_keys

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/neomutt/24944bf7920108f5a4790e6071c32e9102760c37
/usr/share/package-licenses/neomutt/34b2f1d7acba3eeb992e4281307640989cd08d0a
/usr/share/package-licenses/neomutt/b11b797fa13b0935d0e0b13a84f7dd413f9d6ab3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/neomutt.1
/usr/share/man/man1/pgpewrap_neomutt.1
/usr/share/man/man1/smime_keys_neomutt.1
/usr/share/man/man5/mbox_neomutt.5
/usr/share/man/man5/mmdf_neomutt.5
/usr/share/man/man5/neomuttrc.5

%files locales -f neomutt.lang
%defattr(-,root,root,-)

