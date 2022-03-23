#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-console
Version  : 42.beta
Release  : 1
URL      : https://download.gnome.org/sources/gnome-console/42/gnome-console-42.beta.tar.xz
Source0  : https://download.gnome.org/sources/gnome-console/42/gnome-console-42.beta.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-console-bin = %{version}-%{release}
Requires: gnome-console-data = %{version}-%{release}
Requires: gnome-console-lib = %{version}-%{release}
Requires: gnome-console-license = %{version}-%{release}
Requires: gnome-console-locales = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : nautilus-dev
BuildRequires : pcre2-dev
BuildRequires : pkgconfig(libgtop-2.0)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(libnautilus-extension)
BuildRequires : pkgconfig(vte-2.91)
BuildRequires : sassc
BuildRequires : vte-dev

%description
# Console
![](logo.png)
A minimal terminal for GNOME
Console is supposed to be a simple terminal emulator for the average user to carry out simple cli tasks and aims to be a ‘core’ app for GNOME/Phosh

%package bin
Summary: bin components for the gnome-console package.
Group: Binaries
Requires: gnome-console-data = %{version}-%{release}
Requires: gnome-console-license = %{version}-%{release}

%description bin
bin components for the gnome-console package.


%package data
Summary: data components for the gnome-console package.
Group: Data

%description data
data components for the gnome-console package.


%package lib
Summary: lib components for the gnome-console package.
Group: Libraries
Requires: gnome-console-data = %{version}-%{release}
Requires: gnome-console-license = %{version}-%{release}

%description lib
lib components for the gnome-console package.


%package license
Summary: license components for the gnome-console package.
Group: Default

%description license
license components for the gnome-console package.


%package locales
Summary: locales components for the gnome-console package.
Group: Default

%description locales
locales components for the gnome-console package.


%prep
%setup -q -n gnome-console-42.beta
cd %{_builddir}/gnome-console-42.beta

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648058725
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-console
cp %{_builddir}/gnome-console-42.beta/COPYING %{buildroot}/usr/share/package-licenses/gnome-console/338650eb7a42dd9bc1f1c6961420f2633b24932d
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang kgx

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kgx

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Console.desktop
/usr/share/dbus-1/services/org.gnome.Console.service
/usr/share/glib-2.0/schemas/org.gnome.Console.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Console.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Console-symbolic.svg
/usr/share/metainfo/org.gnome.Console.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/nautilus/extensions-3.0/libkgx-nautilus.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-console/338650eb7a42dd9bc1f1c6961420f2633b24932d

%files locales -f kgx.lang
%defattr(-,root,root,-)

