Name:           plexmediaplayer
Version:        2.28.0
Release:        1%{?dist}
Summary:        Plex Media Player for Fedora 28+

License:        GPLv2
URL:            https://plex.tv/
# See: https://fedoraproject.org/wiki/Packaging:SourceURL?rd=Packaging/SourceURL#Git_Tags
Source0:        https://github.com/plexinc/plex-media-player/archive/v2.28.0.952-5408ca22.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Source3:        %{name}.service
Source4:        %{name}.target
Source5:        %{name}.pkla.disabled
Source6:        %{name}-standalone
Source7:        %{name}.te
Source8:        %{name}.pp
Source9:       %{name}-standalone-enable

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mpv-libs
BuildRequires:  mpv-libs-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  SDL2-devel
BuildRequires:  libcec-devel >= 4.0.0
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel >= 5.9.5
BuildRequires:  qt5-qtdeclarative-devel >= 5.9.5
BuildRequires:  qt5-qtwebchannel-devel >= 5.9.5
BuildRequires:  qt5-qtwebengine-devel >= 5.9.5
BuildRequires:  qt5-qtx11extras-devel >= 5.9.5

Requires:       mpv-libs
Requires:       libdrm
Requires:       mesa-libGL
Requires:       SDL2
Requires:       libcec >= 4.0.0
Requires:       minizip
Requires:       opencv-core
Requires:       qt5-qtbase >= 5.9.5
Requires:       qt5-qtbase-gui >= 5.9.5
Requires:       qt5-qtdeclarative >= 5.9.5
Requires:       qt5-qtwebchannel >= 5.9.5
Requires:       qt5-qtwebengine >= 5.9.5
Requires:       qt5-qtx11extras >= 5.9.5
Requires:       qt5-qtquickcontrols >= 5.9.5
# User creation.
Requires(pre):  shadow-utils

%description
Plex Media Player - Client for Plex Media Server.

%prep
#%setup -n %{name}-%{version} -q
%setup -n plex-media-player-2.28.0.952-5408ca22 -q

%build
rm -Rf build
mkdir build
cd build
cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DQTROOT=/usr/lib64/qt5 -DMPV_INCLUDE_DIR=/usr/include/mpv -DMPV_LIBRARY=/usr/lib64/libmpv.so.1 -DLINUX_DBUS=ON -DCMAKE_INSTALL_PREFIX=/usr ..
ninja-build

%install
rm -rf $RPM_BUILD_ROOT

cd build
DESTDIR=%{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch} ninja-build install
cd ../

%{__mkdir_p} %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_bindir}
%{__install} -m0755 %{_builddir}/%{buildsubdir}/build/src/plexmediaplayer %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_bindir}/plexmediaplayer
%{__install} -m0755 %{_builddir}/%{buildsubdir}/build/src/pmphelper       %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_bindir}/pmphelper
%{__install} -m0755 %{_sourcedir}/%{name}-standalone                      %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_bindir}/%{name}-standalone

appstream-util validate-relax --nonet %{_sourcedir}/%{name}.appdata.xml
%{__mkdir_p} %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/appdata
%{__install} -m0644 %{_sourcedir}/%{name}.appdata.xml                     %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/appdata/%{name}.appdata.xml

%{__mkdir_p} %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/%{name}
%{__install} -m0755 %{_sourcedir}/%{name}-standalone-enable               %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/%{name}/%{name}-standalone-enable

%{__mkdir_p} %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/%{name}/selinux
%{__install} -m0644 %{_sourcedir}/%{name}.te                              %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/%{name}/selinux/%{name}.te
%{__install} -m0644 %{_sourcedir}/%{name}.pp                              %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/%{name}/selinux/%{name}.pp

%{__mkdir_p} %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_prefix}/lib/systemd/system
%{__install} -m0644 %{_sourcedir}/%{name}.service                         %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_prefix}/lib/systemd/system/%{name}.service
%{__install} -m0644 %{_sourcedir}/%{name}.target                          %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_prefix}/lib/systemd/system/%{name}.target

%{__mkdir_p} %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_sysconfdir}/polkit-1/localauthority/50-local.d
%{__install} -m0644 %{_sourcedir}/%{name}.pkla.disabled                   %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_sysconfdir}/polkit-1/localauthority/50-local.d/%{name}.pkla.disabled

desktop-file-validate %{_sourcedir}/%{name}.desktop
desktop-file-install --dir=%{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/applications %{_sourcedir}/%{name}.desktop


%files
/usr/bin/plexmediaplayer
/usr/bin/pmphelper
/usr/bin/plexmediaplayer-standalone
/usr/lib/systemd/system/plexmediaplayer.service
/usr/lib/systemd/system/plexmediaplayer.target
/usr/share/appdata/plexmediaplayer.appdata.xml
/usr/share/applications/plexmediaplayer.desktop
/usr/share/icons/hicolor/scalable/apps/plexmediaplayer.svg
/usr/share/plexmediaplayer/plexmediaplayer-standalone-enable
/usr/share/plexmediaplayer/selinux/plexmediaplayer.te
/usr/share/plexmediaplayer/selinux/plexmediaplayer.pp
/usr/share/plexmediaplayer/web-client/*
/etc/polkit-1/localauthority/50-local.d/plexmediaplayer.pkla.disabled


%pre
# Create "plexmediaplayer" if it not already exists.
#
# NEVER delete an user or group created by an RPM package. See:
# https://fedoraproject.org/wiki/Packaging:UsersAndGroups#Allocation_Strategies
/usr/bin/getent passwd plexmediaplayer >/dev/null || \
  /sbin/useradd -r -G dialout,video,lock,audio \
  -d %{_sharedstatedir}/plexmediaplayer --create-home -s /sbin/nologin \
  -c "Plex Media Player (Standalone)" plexmediaplayer
%{__chmod} 0750 %{_sharedstatedir}/plexmediaplayer
%{__chown} plexmediaplayer:plexmediaplayer %{_sharedstatedir}/plexmediaplayer


%post
%{__ln_s} -f %{_prefix}/lib/systemd/system/%{name}.service %{_sysconfdir}/systemd/system/
%{__ln_s} -f %{_prefix}/lib/systemd/system/%{name}.target  %{_sysconfdir}/systemd/system/

touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :


%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :


%changelog
* Fri Feb 22 2019 Jonathan Leroy <jonathan@harrycow.fr> - 2.28.0-1
- We've updated our tooling to provide an improved user experience
- AAC audio streams are no longer automatically converted to AC3, EAC3, or DTS
  during Direct Stream or Transcode when the related Settings > Audio setting is
  enabled. Instead they will play without conversion
- Fixed loss of focus when going to an empty web shows page
- Fixed navigation order after switching to the admin user
- Fixed News and Podcasts directories so they don't touch navigation bar
- Fixed extended info poster not positioned properly

* Sat Feb 16 2019 Jonathan Leroy <jonathan@harrycow.fr> - 2.27.0-1
- Desktop web-client updated to 3.83.1
- Support translation of relative time strings
- Adjusted library page jump bar so more characters can be shown
- Changed user menu from dropdown to full screen modal
- Fixed playback controls not showing the correct duration when
  lightweight seeking
- Fixed possible endless spinner when downloading subtitles
- Fixed player controls sometimes not closing when playing from companion app

* Wed Jan 23 2019 Jonathan Leroy <jonathan@harrycow.fr> - 2.26.0-1
- Added actions menu to Web Shows and Podcasts show preplay pages
- Added Chapter Selection title to chapter selection menu
- Don't show "More..." button when there is only one more item
- Fixed possible error on user switcher screen
- Fixed chapter selection sometimes losing focus at the end of the list
- Fixed Live TV restarting from another position when enabling or
  disabling Closed Captioning
- Fixed some issues with video transcoding when it can direct stream

* Fri Jan 11 2019 Jonathan Leroy <jonathan@harrycow.fr> - 2.25.0-1
- Desktop web-client updated to 3.77.4
- Added extended artist biography on artist preplay
- Fixed podcast/web show episodes being marked as played as soon as playback
  is initiated
- Fixed app settings sometimes wrongly showing an item as selected
- Fixed media provider hubs occasionaly not loading
- Fixed an issue where the application could show a blank screen when all
  servers are unavailable

* Tue Dec 18 2018 Jonathan Leroy <jonathan@harrycow.fr> - 2.24.0-1
- Fixed an issue where signing out or switching users could cause the app to
  freeze
- Fixed an issue where the app could crash when loading a type view
- Fixed an issue where focus would be lost after removing the last item from a
  list
- Fixed as issue where enabling recording all episodes for certain shows could
  return in nothing getting added to the priority list
- Fixed an issue that could cause a blank screen to appear after playback
- Fixed loss of focus on episode preplay in some cases

* Mon Dec 03 2018 Jonathan Leroy <jonathan@harrycow.fr> - 2.23.0-1
- Desktop web-client updated to 3.77.2
- Updated look of playlist/collection posters
- Managed users can no longer change the Automatically Sign In setting
- Improved image upscale quality for episode posters
- Fixed sorting/filtering being reset when deleting item

* Mon Nov 26 2018 Jonathan Leroy <jonathan@harrycow.fr> - 2.22.1-1
- Added recording progress to recording schedule
- Subtitles search modal UI changes
- Fixed player control state when playback starts or pauses without
  application control
- Fixed case where focus was lost when navigating back after changing
  list styles
- Fixed play queue starting playback automatically when app is reopened
- Fixed non-functional action buttons on preplay pages in some circumstances
- Fixed case where focus could be lost when navigating into the dashboard
  types header
- Fixed unavailable indicator on preplay pages when media item file
  is unavailable

* Tue Oct 30 2018 Jonathan Leroy <jonathan@harrycow.fr> - 2.21.0-1
- Improvements to subtitles search results titles
- Added new music player UI for podcasts
- Added Related Episodes hub underneath the Podcasts player
- Watch Later and Recommended support has been removed. Please see: 
  plex.tv/blog/subtitles-and-sunsets-big-improvements-little-housekeeping
- Fixed occasional loss of focus on library page when applying “unplayed” filter
- Fixed settings failing to open in some circumstances
- Fixed zip code not disappearing in News settings after selecting a country
  that doesn’t have zip codes
- Fixed selecting a play queue item occasionally not starting playback

* Wed Oct 03 2018 Jonathan Leroy <jonathan@harrycow.fr> - 2.20.0-1
- Desktop web-client updated to 3.71.1
- Improved stream titles (requires PMS 1.13.8 or higher)
- Block app key shortcuts when entering subtitles search title
- Sped up initial loading dashboard
- Fixed blinking thumbnails when moving between items in photo player
- Fixed missing empty dashboard message for managed/shared users with
  restrictions
- Fixed background being lost when navigating away from news player
- Fixed some edge cases around deleting media that could cause the app to become
  unresponsive
- Fixed Chapter Selection focus box not showing sometimes
- Fixed occasional unexpected focused element in app settings modal after
  closing via pointer click
- Fixed some navigation bugs in home screen media types settings
- Fixed settings changes not being immediately visible in the UI
- Fixed pressing seek buttons during music playback making it impossible to
  bring up player controls afterwards
- Fixed subtitles search modal title button width changing when focused
- Fixed news ads playback putting the app in a broken state
- Fixed progress bar being focusable during ads playback
- Fixed news tags and news feed being visible during ads playback
- Fixed news feed being slightly cut off at the bottom
- Fixed issue preventing companion commands
- Fixed display issues with long stream titles on preplay pages

