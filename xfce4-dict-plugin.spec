Summary:	A dict plugin for Xfce panel
Summary(pl.UTF-8):	Wtyczka dict dla panelu Xfce
Name:		xfce4-dict-plugin
Version:	0.3.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-dict-plugin/%{name}-%{version}.tar.gz
# Source0-md5:	5745be80e6e755412bca9c129e35bd70
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-dict-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= 4.4.0
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

%description -l pl.UTF-8
Za pomocą tej wtyczki można odpytać serwer słownika (zgodny z RFC
2229) w celu wyszukania tłumaczenia lub wyjaśnienia słowa. Można także
wybrać słownik oferowany przez serwer w celu poprawienia wyników.

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

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

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
%attr(755,root,root) %{_bindir}/xfce4-popup-dict
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-dict-plugin
%{_datadir}/xfce4/panel-plugins/dict.desktop
%{_iconsdir}/hicolor/scalable/apps/dict-icon.svg
