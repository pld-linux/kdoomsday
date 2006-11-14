Summary:	KDoomsDay - A countdown applet for the KDE panel
Summary(pl):	KDoomsDay - aplet do odliczania dla panelu KDE
Name:		kdoomsday
Version:	0.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://alioth.debian.org/frs/download.php/930/%{name}-%{version}.tar.gz
# Source0-md5:	0778bced8b5b96900f77222387c86f34
Patch0:		kde-common-LD_quote.patch
URL:		http://alioth.debian.org/projects/kdoomsday/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDoomsDay - A countdown applet for the KDE panel.

%description -l pl
KDoomsDay - aplet do odliczania dla panelu KDE.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
# WTF?
#+ make -f admin/Makefile.common cvs
#*** YOU'RE USING automake (GNU automake) 1.9.6.
#*** KDE requires automake 1.6.1 or newer
#make: *** [cvs] Error 1
#%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/libkdoomsday.la
%attr(755,root,root) %{_libdir}/kde3/libkdoomsday.so
%{_datadir}/apps/kicker/applets/kdoomsday.desktop
