%global glib2_version 2.58.0

# Coverity scan can override this to 0, to skip checking in gtk-doc generated code
%{!?with_docs: %global with_docs 1}

Name: libsoup3
Version: 3.0.4
Release: %autorelease
Summary: Soup, an HTTP library implementation

License: LGPLv2
URL: https://wiki.gnome.org/Projects/libsoup
Source0: https://download.gnome.org/sources/libsoup/3.0/libsoup-%{version}.tar.xz
Patch0: xgettext.patch

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: glib-networking
%if %{with_docs}
BuildRequires: gtk-doc
%endif
BuildRequires: krb5-devel
BuildRequires: meson
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(sysprof-capture-4)
BuildRequires: vala
BuildRequires: /usr/bin/ntlm_auth
BuildRequires: pkgconfig(libnghttp2)

Recommends: glib-networking%{?_isa} >= %{glib2_version}

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it), but the SOAP parts were removed
long ago.

%package devel
Summary: Header files for the Soup library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Libsoup is an HTTP library implementation in C. This package allows
you to develop applications that use the libsoup library.

%if %{with_docs}

%package doc
Summary: Documentation files for %{name}
BuildArch: noarch

%description doc
This package contains developer documentation for %{name}.

%endif

%prep
%autosetup -p0 -n libsoup-%{version}

%build
%if %{with_docs}
%global gtkdoc_flags -Dgtk_doc=true
%else
%global gtkdoc_flags -Dgtk_doc=false
%endif

%meson %gtkdoc_flags -Dtests=false -Dautobahn=disabled -Dhttp2_tests=disabled -Dpkcs11_tests=disabled
%meson_build

%install
%meson_install

%find_lang libsoup-3.0

%files -f libsoup-3.0.lang
%license COPYING
%doc README NEWS AUTHORS
%{_libdir}/libsoup-3.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Soup*3.0.typelib

%files devel
%{_includedir}/libsoup-3.0
%{_libdir}/libsoup-3.0.so
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Soup*3.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libsoup-3.0.deps
%{_datadir}/vala/vapi/libsoup-3.0.vapi

%if %{with_docs}

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libsoup-3.0

%endif

%changelog
%autochangelog
