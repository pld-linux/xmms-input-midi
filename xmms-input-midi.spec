Summary:	Midi file player Plug-In for xmms
Summary(pl):	Wtyczka odtwarzaj±ca pliki midi
Name:		xmms-input-midi
Version:	0.03
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://ban.joh.cam.ac.uk/~cr212/xmms-midi/xmms-midi-%{version}.tar.gz
# Source0-md5:	a35c62378fc3ccdf420fe81636e5b2f8
URL:		http://ban.joh.cam.ac.uk/~cr212/xmms-midi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xmms-devel
Requires:	TiMidity++-instruments
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugin_dir	%(xmms-config --input-plugin-dir)

%description
Midi file player Plug-In for xmms.

%description -l pl
Wtyczka odtwarzaj±ca pliki midi.

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
	xmmsinputdir=%{plugin_dir}

# useless
rm -f $RPM_BUILD_ROOT%{plugin_dir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{plugin_dir}/*.so
