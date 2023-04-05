#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	LV2 (LADSPA Version 2) Audio Plugin Standard
Summary(pl.UTF-8):	LV2 (LADSPA Version 2) - standard wtyczek dźwiękowych
Name:		lv2
Version:	1.18.10
Release:	1
License:	ISC
Group:		Libraries
Source0:	https://lv2plug.in/spec/%{name}-%{version}.tar.xz
# Source0-md5:	9c1f3143ea2eea341e8d6e1bad9e5e0e
URL:		https://lv2plug.in/
# for eg-scope ui
BuildRequires:	cairo-devel >= 1.8.10
# for eg-sampler and eg-scope ui
BuildRequires:	gtk+2-devel >= 2:2.18.0
# for eg-sampler
BuildRequires:	libsamplerate-devel >= 0.1.0
# for eg-sampler
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.7
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	python3-lxml
BuildRequires:	python3-markdown
BuildRequires:	python3-pygments
BuildRequires:	python3-rdflib
%endif
Obsoletes:	lv2core < 8
Obsoletes:	lv2-data-access < 1.6
Obsoletes:	lv2-dynmanifest < 1.4
Obsoletes:	lv2-event < 1.6
Obsoletes:	lv2-instance-access < 1.6
Obsoletes:	lv2-midi < 1.6
Obsoletes:	lv2-presets < 2.6
Obsoletes:	lv2-ui < 2.8
Obsoletes:	lv2-units < 5.6
Obsoletes:	lv2-uri-map < 1.6
Obsoletes:	lv2-urid < 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/lv2

%description
LV2 is a standard for audio systems. It defines a minimal yet
extensible C API for plugin code and a format for plugin "bundles".
See <https://lv2plug.in/> for more information.

This package contains specifications (a C header and/or a schema in
Turtle), documentation generation tools, and example plugins.

%description -l pl.UTF-8
LV2 to standard systemów dźwiękowych. Definiuje minimalne, ale
rozszerzalne API C dla kodu wtyczek oraz format "paczek" wtyczek.
Więcej informacji pod adresem <https://lv2plug.in/>.

Ten pakiet zawiera specyfikacje (plik nagłówkowy C i/lub schemat w
formacie Turtle), narzędzia do generowania dokumentacji oraz
przykładowe wtyczki.

%package devel
Summary:	LV2 API header file
Summary(pl.UTF-8):	Plik nagłówkowy API LV2
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	lv2core-devel < 8
Obsoletes:	lv2-data-access-devel < 1.6
Obsoletes:	lv2-dynmanifest-devel < 1.4
Obsoletes:	lv2-event-devel < 1.6
Obsoletes:	lv2-instance-access-devel < 1.6
Obsoletes:	lv2-midi-devel < 1.6
Obsoletes:	lv2-presets-devel < 2.6
Obsoletes:	lv2-ui-devel < 2.8
Obsoletes:	lv2-units-devel < 5.6
Obsoletes:	lv2-uri-map-devel < 1.6
Obsoletes:	lv2-urid-devel < 1.2

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

%package apidocs
Summary:	LV2 API documentation
Summary(pl.UTF-8):	Dokumentacja API LV2
Group:		Documentation
BuildArch:	noarch

%description apidocs
LV2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API LV2.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3$,%{__python3},' lv2specgen/lv2specgen.py

%build
%meson build \
	%{!?with_apidocs:-Ddocs=disabled}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans
# replace symlinks to %{_libdir}/lv2/* with directories
for p in atom buf-size core data-access dynmanifest event instance-access log midi morph options parameters patch port-groups port-props presets resize-port state time ui units uri-map urid worker lv2plug.in/ns/lv2core ; do
	if [ -L "%{_includedir}/lv2/$p" ]; then
		rm -f "%{_includedir}/lv2/$p"
	fi
done
for p in atom buf-size data-access dynmanifest event instance-access log midi morph options parameters patch port-groups port-props presets resize-port state time uri-map urid worker ; do
	if [ -L "%{_includedir}/lv2/lv2plug.in/ns/ext/$p" ]; then
		rm -f "%{_includedir}/lv2/lv2plug.in/ns/ext/$p"
	fi
done
for p in ui units ; do
	if [ -L "%{_includedir}/lv2/lv2plug.in/ns/extensions/$p" ]; then
		rm -f "%{_includedir}/lv2/lv2plug.in/ns/extensions/$p"
	fi
done

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%dir %{_libdir}/lv2
%dir %{_libdir}/lv2/core.lv2
%{_libdir}/lv2/core.lv2/lv2core.ttl
%{_libdir}/lv2/core.lv2/lv2core.meta.ttl
%{_libdir}/lv2/core.lv2/manifest.ttl
%{_libdir}/lv2/core.lv2/meta.ttl
%{_libdir}/lv2/core.lv2/people.ttl
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
%attr(755,root,root) %{_bindir}/lv2_validate
%{_includedir}/lv2.h
%dir %{_includedir}/lv2
%{_includedir}/lv2/atom
%{_includedir}/lv2/buf-size
%{_includedir}/lv2/core
%{_includedir}/lv2/data-access
%{_includedir}/lv2/dynmanifest
%{_includedir}/lv2/event
%{_includedir}/lv2/instance-access
%{_includedir}/lv2/log
%{_includedir}/lv2/midi
%{_includedir}/lv2/morph
%{_includedir}/lv2/options
%{_includedir}/lv2/parameters
%{_includedir}/lv2/patch
%{_includedir}/lv2/port-groups
%{_includedir}/lv2/port-props
%{_includedir}/lv2/presets
%{_includedir}/lv2/resize-port
%{_includedir}/lv2/state
%{_includedir}/lv2/time
%{_includedir}/lv2/ui
%{_includedir}/lv2/units
%{_includedir}/lv2/uri-map
%{_includedir}/lv2/urid
%{_includedir}/lv2/worker
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
%{_pkgconfigdir}/lv2.pc
%if %{with apidocs}
%attr(755,root,root) %{_bindir}/lv2specgen.py
%{_datadir}/lv2specgen
%endif

%files eg-sampler
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/eg-sampler.lv2
%{_libdir}/lv2/eg-sampler.lv2/*.ttl
%{_libdir}/lv2/eg-sampler.lv2/click.wav
%attr(755,root,root) %{_libdir}/lv2/eg-sampler.lv2/sampler.so
%attr(755,root,root) %{_libdir}/lv2/eg-sampler.lv2/sampler_ui.so

%files eg-scope
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/eg-scope.lv2
%attr(755,root,root) %{_libdir}/lv2/eg-scope.lv2/examploscope.so
%attr(755,root,root) %{_libdir}/lv2/eg-scope.lv2/examploscope_ui.so
%{_libdir}/lv2/eg-scope.lv2/*.ttl

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%dir %{_docdir}/lv2
%{_docdir}/lv2/c
%{_docdir}/lv2/ns
%{_docdir}/lv2/style
%endif
