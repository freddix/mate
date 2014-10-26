Summary:	MATE Desktop Environment
Name:		mate
Version:	1.8
Release:	5
License:	GPL v2
Group:		X11/Applications
# for caja
Requires:	gvfs
Requires:	gvfs-archive
Requires:	gvfs-cdio
Requires:	gvfs-fuse
Requires:	gvfs-mtp
#
Requires:	atril >= %{version}
Requires:	caja >= %{version}
Requires:	caja-extension-document-viewer >= %{version}
Requires:	caja-extension-engrampa >= %{version}
Requires:	caja-extension-gksu >= %{version}
Requires:	caja-extension-image-converter >= %{version}
Requires:	caja-extension-open-terminal >= %{version}
Requires:	caja-extension-sendto >= %{version}
Requires:	caja-extension-share >= %{version}
Requires:	engrampa >= %{version}
Requires:	eom >= %{version}
Requires:	libmatekbd-runtime >= %{version}
Requires:	libmateweather-data >= %{version}
Requires:	marco >= %{version}
Requires:	mate-applet-battstat >= %{version}
Requires:	mate-applet-charpicker >= %{version}
Requires:	mate-applet-cpufreq  >= %{version}
Requires:	mate-applet-drivemount >= %{version}
Requires:	mate-applet-geyes >= %{version}
Requires:	mate-applet-invest >= %{version}
Requires:	mate-applet-multiload >= %{version}
Requires:	mate-applet-stickynotes >= %{version}
Requires:	mate-applet-trash >= %{version}
Requires:	mate-applet-weather >= %{version}
Requires:	mate-backgrounds-desktop >= %{version}
Requires:	mate-calc >= %{version}
Requires:	mate-control-center >= %{version}
Requires:	mate-desktop >= %{version}
Requires:	mate-dialogs >= %{version}
Requires:	mate-media-volume-control >= %{version}
Requires:	mate-media-volume-control-applet >= %{version}
Requires:	mate-menus >= %{version}
Requires:	mate-notification-daemon >= %{version}
Requires:	mate-panel >= %{version}
Requires:	mate-panel-applet-pm-brightness >= %{version}
Requires:	mate-panel-applet-pm-inhibit >= %{version}
Requires:	mate-polkit >= %{version}
Requires:	mate-power-manager >= %{version}
Requires:	mate-screensaver >= %{version}
Requires:	mate-session-manager >= %{version}
Requires:	mate-settings-daemon >= %{version}
Requires:	mate-terminal >= %{version}
Requires:	mate-utils-dictionary >= %{version}
Requires:	mate-utils-disk-usage-analyzer >= %{version}
Requires:	mate-utils-screenshot >= %{version}
Requires:	mate-utils-search-tool >= %{version}
Requires:	pluma >= %{version}
# external
Requires:	gnome-keyring
#
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
MATE desktop.

%prep
%build
%install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

