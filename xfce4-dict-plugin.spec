Summary:	A dict plugin for Xfce panel
Name:		xfce4-dict-plugin
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-dict-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	2ef7f110883a9d9316fd06a1c2a327da
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-dict-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this plugin you can query a dictionary server (see RFC 2229) to
search for the translation or explanation of a word. You can also
choose a dictionary offered by the server to improve your search
results.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-dict-plugin
%{_datadir}/xfce4/panel-plugins/dict.desktop
%{_iconsdir}/hicolor/scalable/apps/dict-icon.svg
