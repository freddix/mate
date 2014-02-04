Summary:	GNOME desktop
Name:		mate
Version:	1.6
Release:	2
License:	GPL v2
Group:		X11/Applications
Requires:	gvfs
Requires:	gvfs-archive
Requires:	gvfs-cdio
Requires:	gvfs-fuse
Requires:	gvfs-mtp
Requires:	libmatekbd-runtime
Requires:	libmateweather-data
Requires:	mate-applet-battstat
Requires:	mate-applet-charpicker
Requires:	mate-applet-cpufreq
Requires:	mate-applet-drivemount
Requires:	mate-applet-geyes
Requires:	mate-applet-multiload
Requires:	mate-applet-stickynotes
Requires:	mate-applet-trash
Requires:	mate-applet-weather
Requires:	mate-backgrounds-desktop
Requires:	mate-calc
Requires:	mate-control-center
Requires:	mate-desktop
Requires:	mate-document-viewer
Requires:	mate-file-archiver
Requires:	mate-file-manager
Requires:	mate-file-manager-extension-document-viewer
Requires:	mate-file-manager-extension-engrampa
Requires:	mate-file-manager-extension-image-converter
Requires:	mate-image-viewer
Requires:	mate-media-volume-control
Requires:	mate-media-volume-control-applet
Requires:	mate-menus
Requires:	mate-notification-daemon
Requires:	mate-panel
Requires:	mate-panel-applet-pm-brightness
Requires:	mate-panel-applet-pm-inhibit
Requires:	mate-polkit
Requires:	mate-power-manager
Requires:	mate-session-manager
Requires:	mate-settings-daemon
Requires:	mate-terminal
Requires:	mate-text-editor
Requires:	mate-utils-dictionary
Requires:	mate-utils-disk-usage-analyzer
Requires:	mate-utils-screenshot
Requires:	mate-utils-search-tool
Requires:	mate-window-manager
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

