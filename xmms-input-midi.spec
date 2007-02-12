Summary:	Midi file player Plug-In for XMMS
Summary(pl.UTF-8):   Wtyczka wejściowa dla XMMS-a odtwarzająca pliki midi
Name:		xmms-input-midi
Version:	0.03
Release:	4
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://ban.joh.cam.ac.uk/~cr212/xmms-midi/xmms-midi-%{version}.tar.gz
# Source0-md5:	a35c62378fc3ccdf420fe81636e5b2f8
URL:		http://ban.joh.cam.ac.uk/~cr212/xmms-midi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	TiMidity++-instruments
# TiMidity++ for /etc/timidity.cfg
Requires:	TiMidity++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Midi file player Plug-In for XMMS.

%description -l pl.UTF-8
Wtyczka wejściowa dla XMMS-a odtwarzająca pliki midi.

%prep
%setup -q -n xmms-midi-%{version}

sed -e "s@AC_INIT.*@AC_INIT(xmms-midi, %{version})\nAM_INIT_AUTOMAKE@" \
	configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make} \
	libmid_la_LDFLAGS="-avoid-version"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	xmmsinputdir=%{xmms_input_plugindir}

# useless
rm -f $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{xmms_input_plugindir}/*.so
