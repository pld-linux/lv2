# TODO: rethink plugins packaging (included or in subpackages? subpackage could include individual NEWS files; for descriptions see lv2-*.spec files)
# core
%define	lv2core_ver			14.0
# ext
%define	lv2_data_access_ver		1.6
%define	lv2_dynmanifest_ver		1.6
%define	lv2_event_ver			1.12
%define	lv2_instance_access_ver		1.6
%define	lv2_midi_ver			1.8
%define	lv2_presets_ver			2.8
%define	lv2_uri_map_ver			1.6
%define	lv2_urid_ver			1.4
# extensions
%define	lv2_ui_ver			2.20
%define	lv2_units_ver			5.10
Summary:	LV2 (LADSPA Version 2) Audio Plugin Standard
Summary(pl.UTF-8):	LV2 (LADSPA Version 2) - standard wtyczek dźwiękowych
Name:		lv2
Version:	1.14.0
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	0b56285a77aac3c93b50c36203aa91ee
URL:		http://lv2plug.in/
# g++ only checked for, not used
BuildRequires:	libstdc++-devel
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
# for eg-scope ui
BuildRequires:	cairo-devel >= 1.8.10
# for eg-sampler and eg-scope ui
BuildRequires:	gtk+2-devel >= 2:2.18.0
# for eg-sampler
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	pkgconfig
Provides:	lv2core = %{lv2core_ver}
Obsoletes:	lv2core < %{lv2core_ver}
Provides:	lv2-data-access = %{lv2_data_access_ver}
Obsoletes:	lv2-data-access < %{lv2_data_access_ver}
Provides:	lv2-dynmanifest = %{lv2_dynmanifest_ver}
Obsoletes:	lv2-dynmanifest < %{lv2_dynmanifest_ver}
Provides:	lv2-event = %{lv2_event_ver}
Obsoletes:	lv2-event < %{lv2_event_ver}
Provides:	lv2-instance-access = %{lv2_instance_access_ver}
Obsoletes:	lv2-instance-access < %{lv2_instance_access_ver}
Provides:	lv2-midi = %{lv2_midi_ver}
Obsoletes:	lv2-midi < %{lv2_midi_ver}
Provides:	lv2-presets = %{lv2_presets_ver}
Obsoletes:	lv2-presets < %{lv2_presets_ver}
Provides:	lv2-ui = %{lv2_ui_ver}
Obsoletes:	lv2-ui < %{lv2_ui_ver}
Provides:	lv2-units = %{lv2_units_ver}
Obsoletes:	lv2-units < %{lv2_units_ver}
Provides:	lv2-uri-map = %{lv2_uri_map_ver}
Obsoletes:	lv2-uri-map < %{lv2_uri_map_ver}
Provides:	lv2-urid = %{lv2_urid_ver}
Obsoletes:	lv2-urid < %{lv2_urid_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 is a standard for audio systems. It defines a minimal yet
extensible C API for plugin code and a format for plugin "bundles".
See <http://lv2plug.in/> for more information.

This package contains specifications (a C header and/or a schema in
Turtle), documentation generation tools, and example plugins.

%description -l pl.UTF-8
LV2 to standard systemów dźwiękowych. Definiuje minimalne, ale
rozszerzalne API C dla kodu wtyczek oraz format "paczek" wtyczek.
Więcej informacji pod adresem <http://lv2plug.in/>.

Ten pakiet zawiera specyfikacje (plik nagłówkowy C i/lub schemat w
formacie Turtle), narzędzia do generowania dokumentacji oraz
przykładowe wtyczki.

%package devel
Summary:	LV2 API header file
Summary(pl.UTF-8):	Plik nagłówkowy API LV2
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	lv2core-devel = %{lv2core_ver}
Obsoletes:	lv2core-devel < %{lv2core_ver}
Provides:	lv2-data-access-devel = %{lv2_data_access_ver}
Obsoletes:	lv2-data-access-devel < %{lv2_data_access_ver}
Provides:	lv2-dynmanifest-devel = %{lv2_dynmanifest_ver}
Obsoletes:	lv2-dynmanifest-devel < %{lv2_dynmanifest_ver}
Provides:	lv2-event-devel = %{lv2_event_ver}
Obsoletes:	lv2-event-devel < %{lv2_event_ver}
Provides:	lv2-instance-access-devel = %{lv2_instance_access_ver}
Obsoletes:	lv2-instance-access-devel < %{lv2_instance_access_ver}
Provides:	lv2-midi-devel = %{lv2_midi_ver}
Obsoletes:	lv2-midi-devel < %{lv2_midi_ver}
Provides:	lv2-presets-devel = %{lv2_presets_ver}
Obsoletes:	lv2-presets-devel < %{lv2_presets_ver}
Provides:	lv2-ui-devel = %{lv2_ui_ver}
Obsoletes:	lv2-ui-devel < %{lv2_ui_ver}
Provides:	lv2-units-devel = %{lv2_units_ver}
Obsoletes:	lv2-units-devel < %{lv2_units_ver}
Provides:	lv2-uri-map-devel = %{lv2_uri_map_ver}
Obsoletes:	lv2-uri-map-devel < %{lv2_uri_map_ver}
Provides:	lv2-urid-devel = %{lv2_urid_ver}
Obsoletes:	lv2-urid-devel < %{lv2_urid_ver}

%description devel
LV2 API header file.

%description devel -l pl.UTF-8
Plik nagłówkowy API LV2.

%package eg-sampler
Summary:	Sampler example plugin for LV2
Summary(pl.UTF-8):	Przykładowa wtyczka dla LV2: Sampler
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.18.0
Requires:	libsndfile >= 1.0.0

%description eg-sampler
Sampler example plugin for LV2.

%description eg-sampler -l pl.UTF-8
Przykładowa wtyczka dla LV2: Sampler.

%package eg-scope
Summary:	Simple Oscilloscope example plugin for LV2
Summary(pl.UTF-8):	Przykładowa wtyczka dla LV2: prosty oscyloskop
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo >= 1.8.10
Requires:	gtk+2 >= 2:2.18.0

%description eg-scope
Simple oscilloscope example plugin for LV2.

%description eg-scope -l pl.UTF-8
Przykładowa wtyczka dla LV2: prosty oscyoloskop.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--lv2dir=%{_libdir}/lv2
./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lv2/atom.lv2/atom-test.c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%dir %{_libdir}/lv2
%dir %{_libdir}/lv2/lv2core.lv2
%{_libdir}/lv2/lv2core.lv2/lv2core.ttl
%{_libdir}/lv2/lv2core.lv2/lv2core.doap.ttl
%{_libdir}/lv2/lv2core.lv2/manifest.ttl
%dir %{_libdir}/lv2/atom.lv2
%{_libdir}/lv2/atom.lv2/*.ttl
%dir %{_libdir}/lv2/buf-size.lv2
%{_libdir}/lv2/buf-size.lv2/*.ttl
%dir %{_libdir}/lv2/data-access.lv2
%{_libdir}/lv2/data-access.lv2/*.ttl
%dir %{_libdir}/lv2/dynmanifest.lv2
%{_libdir}/lv2/dynmanifest.lv2/*.ttl
%dir %{_libdir}/lv2/eg-amp.lv2
%{_libdir}/lv2/eg-amp.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/eg-amp.lv2/amp.so
%dir %{_libdir}/lv2/eg-fifths.lv2
%{_libdir}/lv2/eg-fifths.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/eg-fifths.lv2/fifths.so
%dir %{_libdir}/lv2/eg-metro.lv2
%{_libdir}/lv2/eg-metro.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/eg-metro.lv2/metro.so
%dir %{_libdir}/lv2/eg-midigate.lv2
%{_libdir}/lv2/eg-midigate.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/eg-midigate.lv2/midigate.so
%dir %{_libdir}/lv2/eg-params.lv2
%{_libdir}/lv2/eg-params.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/eg-params.lv2/params.so
%dir %{_libdir}/lv2/event.lv2
%{_libdir}/lv2/event.lv2/*.ttl
%dir %{_libdir}/lv2/instance-access.lv2
%{_libdir}/lv2/instance-access.lv2/*.ttl
%dir %{_libdir}/lv2/log.lv2
%{_libdir}/lv2/log.lv2/*.ttl
%dir %{_libdir}/lv2/midi.lv2
%{_libdir}/lv2/midi.lv2/*.ttl
%dir %{_libdir}/lv2/morph.lv2
%{_libdir}/lv2/morph.lv2/*.ttl
%dir %{_libdir}/lv2/options.lv2
%{_libdir}/lv2/options.lv2/*.ttl
%dir %{_libdir}/lv2/parameters.lv2
%{_libdir}/lv2/parameters.lv2/*.ttl
%dir %{_libdir}/lv2/patch.lv2
%{_libdir}/lv2/patch.lv2/*.ttl
%dir %{_libdir}/lv2/port-groups.lv2
%{_libdir}/lv2/port-groups.lv2/*.ttl
%dir %{_libdir}/lv2/port-props.lv2
%{_libdir}/lv2/port-props.lv2/*.ttl
%dir %{_libdir}/lv2/presets.lv2
%{_libdir}/lv2/presets.lv2/*.ttl
%dir %{_libdir}/lv2/resize-port.lv2
%{_libdir}/lv2/resize-port.lv2/*.ttl
%dir %{_libdir}/lv2/schemas.lv2
%{_libdir}/lv2/schemas.lv2/*.ttl
%dir %{_libdir}/lv2/state.lv2
%{_libdir}/lv2/state.lv2/*.ttl
%dir %{_libdir}/lv2/time.lv2
%{_libdir}/lv2/time.lv2/*.ttl
%dir %{_libdir}/lv2/ui.lv2
%{_libdir}/lv2/ui.lv2/*.ttl
%dir %{_libdir}/lv2/units.lv2
%{_libdir}/lv2/units.lv2/*.ttl
%dir %{_libdir}/lv2/uri-map.lv2
%{_libdir}/lv2/uri-map.lv2/*.ttl
%dir %{_libdir}/lv2/urid.lv2
%{_libdir}/lv2/urid.lv2/*.ttl
%dir %{_libdir}/lv2/worker.lv2
%{_libdir}/lv2/worker.lv2/*.ttl

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lv2specgen.py
%{_libdir}/lv2/lv2core.lv2/lv2.h
%{_libdir}/lv2/atom.lv2/*.h
%{_libdir}/lv2/buf-size.lv2/buf-size.h
%{_libdir}/lv2/data-access.lv2/data-access.h
%{_libdir}/lv2/dynmanifest.lv2/dynmanifest.h
%{_libdir}/lv2/event.lv2/event*.h
%{_libdir}/lv2/instance-access.lv2/instance-access.h
%{_libdir}/lv2/log.lv2/log.h
%{_libdir}/lv2/log.lv2/logger.h
%{_libdir}/lv2/midi.lv2/midi.h
%{_libdir}/lv2/morph.lv2/morph.h
%{_libdir}/lv2/options.lv2/options.h
%{_libdir}/lv2/parameters.lv2/parameters.h
%{_libdir}/lv2/patch.lv2/patch.h
%{_libdir}/lv2/port-groups.lv2/port-groups.h
%{_libdir}/lv2/port-props.lv2/port-props.h
%{_libdir}/lv2/presets.lv2/presets.h
%{_libdir}/lv2/resize-port.lv2/resize-port.h
%{_libdir}/lv2/state.lv2/state.h
%{_libdir}/lv2/time.lv2/time.h
%{_libdir}/lv2/ui.lv2/ui.h
%{_libdir}/lv2/units.lv2/units.h
%{_libdir}/lv2/uri-map.lv2/uri-map.h
%{_libdir}/lv2/urid.lv2/urid.h
%{_libdir}/lv2/worker.lv2/worker.h
%{_includedir}/lv2.h
%dir %{_includedir}/lv2
%dir %{_includedir}/lv2/lv2plug.in
%dir %{_includedir}/lv2/lv2plug.in/ns
%{_includedir}/lv2/lv2plug.in/ns/lv2core
%dir %{_includedir}/lv2/lv2plug.in/ns/ext
%{_includedir}/lv2/lv2plug.in/ns/ext/atom
%{_includedir}/lv2/lv2plug.in/ns/ext/buf-size
%{_includedir}/lv2/lv2plug.in/ns/ext/data-access
%{_includedir}/lv2/lv2plug.in/ns/ext/dynmanifest
%{_includedir}/lv2/lv2plug.in/ns/ext/event
%{_includedir}/lv2/lv2plug.in/ns/ext/instance-access
%{_includedir}/lv2/lv2plug.in/ns/ext/log
%{_includedir}/lv2/lv2plug.in/ns/ext/midi
%{_includedir}/lv2/lv2plug.in/ns/ext/morph
%{_includedir}/lv2/lv2plug.in/ns/ext/options
%{_includedir}/lv2/lv2plug.in/ns/ext/parameters
%{_includedir}/lv2/lv2plug.in/ns/ext/patch
%{_includedir}/lv2/lv2plug.in/ns/ext/port-groups
%{_includedir}/lv2/lv2plug.in/ns/ext/port-props
%{_includedir}/lv2/lv2plug.in/ns/ext/presets
%{_includedir}/lv2/lv2plug.in/ns/ext/resize-port
%{_includedir}/lv2/lv2plug.in/ns/ext/state
%{_includedir}/lv2/lv2plug.in/ns/ext/time
%{_includedir}/lv2/lv2plug.in/ns/ext/uri-map
%{_includedir}/lv2/lv2plug.in/ns/ext/urid
%{_includedir}/lv2/lv2plug.in/ns/ext/worker
%dir %{_includedir}/lv2/lv2plug.in/ns/extensions
%{_includedir}/lv2/lv2plug.in/ns/extensions/ui
%{_includedir}/lv2/lv2plug.in/ns/extensions/units
%{_datadir}/lv2specgen
%{_pkgconfigdir}/lv2.pc
%{_pkgconfigdir}/lv2core.pc

%files eg-sampler
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/eg-sampler.lv2
%{_libdir}/lv2/eg-sampler.lv2/*.ttl
%{_libdir}/lv2/eg-sampler.lv2/click.wav
%attr(755,root,root) %{_libdir}/lv2/eg-sampler.lv2/sampler*.so

%files eg-scope
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/eg-scope.lv2
%attr(755,root,root) %{_libdir}/lv2/eg-scope.lv2/examploscope.so
%attr(755,root,root) %{_libdir}/lv2/eg-scope.lv2/examploscope_ui.so
%dir %{_libdir}/lv2/eg-scope.lv2/*.ttl
