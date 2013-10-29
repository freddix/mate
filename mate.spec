Summary:	GNOME desktop
Name:		mate
Version:	1.6
Release:	0.11
License:	GPL v2
Group:		X11/Applications
Requires:	gvfs
Requires:	gvfs-archive
Requires:	gvfs-cdio
Requires:	gvfs-dnssd
Requires:	gvfs-fuse
Requires:	gvfs-mtp
Requires:	gvfs-smb
Requires:	libmatekbd-runtime
Requires:	libmateweather-data
Requires:	mate-backgrounds-desktop
Requires:	mate-control-center
Requires:	mate-desktop
Requires:	mate-file-manager
Requires:	mate-menus
Requires:	mate-panel
Requires:	mate-polkit
Requires:	mate-session-manager
Requires:	mate-settings-daemon
Requires:	mate-terminal
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

