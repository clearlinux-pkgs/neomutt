#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : neomutt
Version  : 20230517
Release  : 22
URL      : https://github.com/neomutt/neomutt/archive/20230517/neomutt-20230517.tar.gz
Source0  : https://github.com/neomutt/neomutt/archive/20230517/neomutt-20230517.tar.gz
Summary  : A version of mutt with added features
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: neomutt-bin = %{version}-%{release}
Requires: neomutt-data = %{version}-%{release}
Requires: neomutt-libexec = %{version}-%{release}
Requires: neomutt-license = %{version}-%{release}
Requires: neomutt-locales = %{version}-%{release}
Requires: neomutt-man = %{version}-%{release}
BuildRequires : buildreq-configure
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Disable-error-on-invalid-configure-item.patch

%description
NeoMutt is a command line mail reader (or MUA). It is a fork of Mutt with added
features. The NeoMutt project is hoping to kick-start development on the Mutt
project. NeoMutt has already attracted about twenty developers and enthusiasts.
Lots of old Mutt patches have been brought up-to-date, tidied and documented.
Notably, the Sidebar patch has now been adopted by upstream Mutt.

%package bin
Summary: bin components for the neomutt package.
Group: Binaries
Requires: neomutt-data = %{version}-%{release}
Requires: neomutt-libexec = %{version}-%{release}
Requires: neomutt-license = %{version}-%{release}

%description bin
bin components for the neomutt package.


%package data
Summary: data components for the neomutt package.
Group: Data

%description data
data components for the neomutt package.


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
%setup -q -n neomutt-20230517
cd %{_builddir}/neomutt-20230517
%patch1 -p1
pushd ..
cp -a neomutt-20230517 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685591065
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
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
popd
%install
export SOURCE_DATE_EPOCH=1685591065
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/neomutt
cp %{_builddir}/neomutt-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/neomutt/b11b797fa13b0935d0e0b13a84f7dd413f9d6ab3 || :
cp %{_builddir}/neomutt-%{version}/autosetup/LICENSE %{buildroot}/usr/share/package-licenses/neomutt/34b2f1d7acba3eeb992e4281307640989cd08d0a || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang neomutt
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/neomutt
/usr/bin/neomutt

%files data
%defattr(-,root,root,-)
/usr/share/neomutt/account-command/README.md
/usr/share/neomutt/account-command/gpg-json/README.md
/usr/share/neomutt/account-command/gpg-json/credentials.sh
/usr/share/neomutt/account-command/macos-keychain/README.md
/usr/share/neomutt/account-command/macos-keychain/keychain.py
/usr/share/neomutt/colorschemes/neonwolf-256.neomuttrc
/usr/share/neomutt/colorschemes/solarized-dark-256.neomuttrc
/usr/share/neomutt/colorschemes/vombatidae.neomuttrc
/usr/share/neomutt/colorschemes/zenburn.neomuttrc
/usr/share/neomutt/logo/neomutt-128.png
/usr/share/neomutt/logo/neomutt-256.png
/usr/share/neomutt/logo/neomutt-32.png
/usr/share/neomutt/logo/neomutt-64.png
/usr/share/neomutt/logo/neomutt.svg
/usr/share/neomutt/mime.types
/usr/share/neomutt/oauth2/mutt_oauth2.py
/usr/share/neomutt/oauth2/mutt_oauth2.py.README
/usr/share/neomutt/vim-keys/README.md
/usr/share/neomutt/vim-keys/vim-keys.rc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/neomutt/*

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/neomutt/pgpewrap
/usr/libexec/neomutt/pgpewrap
/usr/libexec/neomutt/smime_keys

%files license
%defattr(0644,root,root,0755)
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

