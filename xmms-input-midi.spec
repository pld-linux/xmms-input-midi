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

%build
CC="%{__cc}" CFLAGS="%{rpmcflags}" ./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugin_dir}

install .libs/libmid.so.0.0.0 $RPM_BUILD_ROOT%{plugin_dir}/libmid.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{plugin_dir}/*
