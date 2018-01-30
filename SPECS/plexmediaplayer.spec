Name:           plexmediaplayer
Version:        2.3.0
Release:        1%{?dist}
Summary:        Plex Media Player for Fedora 25+

License:        GPLv2
URL:            https://plex.tv/
# See: https://fedoraproject.org/wiki/Packaging:SourceURL?rd=Packaging/SourceURL#Git_Tags
Source0:        https://github.com/plexinc/plex-media-player/archive/v2.3.0.774-ef2108c2.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# https://raw.githubusercontent.com/plexinc/plex-media-player/master/resources/images/icon.png
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Source4:        %{name}.service
Source5:        %{name}.target
Source6:        %{name}.pkla.disabled
Source7:        %{name}-standalone
Source8:        %{name}.te
Source9:        %{name}.pp
Source10:       %{name}-standalone-enable
Patch0:         %{name}-qtwebengine.patch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python-pip
BuildRequires:  mpv-libs
BuildRequires:  mpv-libs-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  SDL2-devel
BuildRequires:  libcec-devel >= 4.0.0
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel >= 5.7
BuildRequires:  qt5-qtdeclarative-devel >= 5.7
BuildRequires:  qt5-qtwebchannel-devel >= 5.7
BuildRequires:  qt5-qtwebengine-devel >= 5.7
BuildRequires:  qt5-qtx11extras-devel >= 5.7

Requires:       mpv-libs
Requires:       libdrm
Requires:       mesa-libGL
Requires:       SDL2
Requires:       libcec >= 4.0.0
Requires:       minizip
Requires:       opencv-core
Requires:       qt5-qtbase >= 5.7
Requires:       qt5-qtbase-gui >= 5.7
Requires:       qt5-qtdeclarative >= 5.7
Requires:       qt5-qtwebchannel >= 5.7
Requires:       qt5-qtwebengine >= 5.7
Requires:       qt5-qtx11extras >= 5.7
Requires:       qt5-qtquickcontrols >= 5.7
# User creation.
Requires(pre):  shadow-utils

%description
Plex Media Player - Client for Plex Media Server.

%prep
# Dirty hack to make conan work in Copr.
pip install --user conan
conan remote add plex https://conan.plex.tv

#%setup -n %{name}-%{version} -q
%setup -n plex-media-player-2.3.0.774-ef2108c2 -q
%patch0 -p0

%build
rm -Rf build
mkdir build
cd build
conan install ..
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

%{__mkdir_p} %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/icons/hicolor/256x256/apps
%{__install} -m0644 %{_sourcedir}/%{name}.png                             %{_buildrootdir}/%{name}-%{version}-%{release}.%{_arch}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

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
/usr/share/icons/hicolor/256x256/apps/plexmediaplayer.png
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
* Tue Jan 30 2018 Jonathan Leroy <jonathan@harrycow.fr> - 2.3.0-1
- Channels are now referred to as Plugins
- Added default posters for artists/albums without artwork in search results
- Added automatic fallback to transcode if direct stream video fails
- Photos will display at a maximum resolution of 1920x1080
- Fixed possible crash when exiting players
- Fixed bitrate display issues. Music and smaller video bitrates should now display in kbps
- Fixed the app crashing when photo strip in photo player is focused
- Fixed photo player strip cells popping in and sometimes showing incorrect images
- Fixed the playlist page displaying incorrect name and duration
- Fixed the text case in the header music player and user menu button
- Fixed the player controls menu ("•••") button not being disabled for watch later/recommended/channel videos
- Fixed the "Unavailable" badge not being consistently displayed in preplay pages
- Fixed videos in playlists not prompting to resume
- Fixed photo slideshows from photo channels not playing all photos
- Fixed player key handling when OSD is hidden
- Fixed the user sometimes not being able to focus the photo strip when viewing photos from channels
- Fixed theme music not stopping when browsing between search and preplay pages
- Disabling logging to the Plex Media Server correctly prevents sending of log messages to the media server
- Artist poster images are aligned at the top edge
- Subtitles toggle alert shows stream metadata
- Lyrics are only available for the current playing track in the play queue
- Player controls do not jump around when the durations change
- Fixed companion video control in mixed photo/video libraries
- Fixed some details in music playback such as the metadata using the album artist rather than the track artist and OSD appearing during track changes
- Fixed the post play disappearing after screensaver is dismissed
- Fixed titles sometimes unnecessarily scrolling
- Restore focus correctly in season details episodes list after playback
- Fixed audio / video not playing when bandwidth restrictions and attempting to direct play
- Fixed the first enter press when the player controls are hidden showing the controls and executing the active button action immediately

* Sat Sep 30 2017 Jonathan Leroy <jonathan@harrycow.fr> - 2.1.1-1
- Navigating back to library list and grid view restores the last focused position
- Change screensaver behavior to reduce load on underlying system
- The application should display without visual artifacts on high DPI screens
- Videos should no longer render with a red shift
- The update channel labels have been renamed to align with product lifecycle. The "Plex Pass" update channel will be labeled "Beta"
- Fix the background sometimes not being restored after exiting the photo player
- Correct trouble saving settings introduced in the first PMP preview release
- The equalizer icon shown when music is playing is back to animating during playback
- Return to the Home dashboard when using the Home icon or navigate home keyboard shortcut
- Pressing the Play button on your remote control will automatically resume playback when asked to decide whether to resume or restart a video
- Selecting Go To Artist from a track in the music player no longer navigates to the version 1 view
- Desktop web-client updated to 3.20.6

* Mon Aug 21 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.3.5-1
- Desktop web-client updated to 3.14.1
- Fix errors when opening the player (Desktop)

* Sun Jul 02 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.3.4-1
- Desktop web-client updated to 3.9.1

* Sat Jun 10 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.3.3-1
- Fix plaxback with optical device type and AC3 enabled
- Fix direct play with some DVR recordings (LATM)

* Sun May 28 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.3.2-1
- Desktop web-client updated to 3.7.0
- Fix casting to Plex Media Player

* Sat May 20 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.3.1-1
- Desktop web-client updated to 3.6.0
- Reverted QT to 5.7

* Sat May 20 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.3.0-1
- Desktop web-client updated to 3.5.0
- TV web-client updated to 3.3.0
- Updated QT to 5.8
- Updated Dependencies
- Fix LIRC keyup detection

* Sat May 20 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.2.5-1
- TV interface not using full window size

* Sat May 20 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.2.4-1
- Updated dependencies
- Fix HLS issue

* Sat May 20 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.2.3-1
- Desktop web-client updated to 3.0.1
- TV web-client updated to 2.13.1
- Add an experimental setting to force what screen PMP should be shown on in fullscreen
- Add experimental refreshrate.avoid_25hz_30hz and audio_delay.50hz hidden settings
- Media key support
- Mark as watched/unwatched on recently played items
- Fixed translations
- Fixes to autorepeat handling (includes fixing accidental pausing when starting playback)

* Sun Jan 08 2017 Jonathan Leroy <jonathan@harrycow.fr> - 1.2.2-1
- Desktop web-client updated to 2.12.6
- TV web-client updated to 2.10.8-fd540f9
- Added better companion support for certain devices
- Fixed respect automatically update setting

* Wed Dec 21 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.2.1-2
- Remove unnecessary file
- Fix standalone mode script

* Tue Dec 20 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.2.1-1
- Desktop web-client updated to 2.12.5
- TV web-client updated to 2.10.8-9a2e1fb
- Multimedia keys (play, next, prev) now work in desktop mode
- Changes to mode switching. There is now a new setting called "layout" which can be set to "tv" or "auto". Auto will behave as 1.2.0 and switch to TV mode when in fullscreen. Set this to TV to "lock" the tv layout and not automatically switch to desktop mode. This can also be set by adding --tv to the command line
- Added new command line switch to control the scale factor of the UI --scale-factor=X
- New subtitle color added
- Automatic subtitle encoding detection
- Prevent screensaver during video/photo playback
- Respect video quality setting
- Support for HiDPI mode
- Various playback related fixes
- libCEC 4 support, thanks to LongChair (https://github.com/LongChair)

* Tue Dec 20 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.2.0-2
- Add missing qt5-qtquickcontrols dependencie
- Add QT_SCALE_FACTOR environment variable in plexmediaplayer-standalone script

* Tue Dec 20 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.2.0-1
- Add a desktop UI mode
- Fix enabling audio passthrough on new installations
- Fix music playback failures in some corner cases

* Sun Dec 18 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.7-1
- Removed the "Advanced" checkbox in the audio settings. PMP now behaves the same as if "Advanced" was always enabled in previous versions
- Added a new "copy-back" hardware decoding setting. Useful only in specific situations
- Fix screensaver behavior. In particular, the screensaver should now also start before any videos were played
- Subtitle selection for vobsubs with multiple stream should now finally work
- Fix rate display mode auto switching with imprecise media FPS values values like 24.999 (and the same for imprecise display refresh rates)
- Fix subtitle/audio stream selection failure under certain circumstances. Requires at least server version 1.2.1
- Fixed remote control compatibility with latest version of Plex for iOS
- Progress when playing back mp3's didn't always update

* Sat Oct 08 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.6-1
- Updated web-client to 2.10.0
- Added always on top setting (thanks to Lukas Pitschl)
- Enabled power options on Embedded x86 (thanks to Jonathan Leroy)
- PMP now selects multi-channel audio over stereo if your system is configured for more channels than 2 in settings
- Add audio_delay.25hz setting for tweaking audio delay for 25hz mode
- Add new mode to force 16:9 aspect ratio for 4:3 video
- Audio now does not always force upmixing, e.g. playing stereo even if 7.1 is configured. To enable this you need to go and reselect the number of channels in audio configuration
- Fixed respawning helper process
- Fixed a bug where going into fullscreen could end up in a bad loop
- Subtitle selection for vobsubs should now work
- Crash fixes

* Tue Aug 09 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.4-1
- Changing aspect ratio during playback could halt playback
- Fix volume up with "+" on some keyboards
- Playback sometimes did not end
- Issues with msmpeg and wmv1 codecs on some platforms

* Thu Aug 04 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.3-3
- Pass parameters to xinit instead of using a ~/.xinitrc file
- Remove dbus-launch from plexmediaplayer-standalone script

* Thu Aug 04 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.3-2
- Missing web client files
- X server no longer power off screen on standalone mode

* Wed Aug 03 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.3-1
- Qt bumped to version 5.7.0
- Change how web-client is bundled
- Missing Minizip dependency
- Remove invalid "--standalone" parameter in plexmediaplayer-standalone script

* Mon Jun 27 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.2-2
- Remove workaround for issue #244.

* Sun Jun 19 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.2-1
- There was an issue where the web-client and the playback engine could get out of state and cause screensaver to show up during movies or not let you press play/pause. This is now fixed
- Non US locales could create problems with playback on Linux
- CEC keyhandling is now back to the default (no auto-repeat) beacuse of many incompatibilities. If you have a CEC device that gives you press and release events you can enable autorepeat by editing the configuration file
- PMP can now be built with Qt 5.7
- Screensaver should be smooth again

* Thu May 12 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.1-2
- Missing OpenCV dependency.

* Thu May 12 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.1.1-1
- Search window now handle keyboard input
- Emulated Roku 3 HTTP Input
- All inputs now handle accelerated auto-repeat
- Support for Plex Home Theater harmony mode
- Clock in both navigation and Player UI
- Cycle zoom options with the Z key
- Support for hiding power options by editing the configuration file
- Some keymappings changed, fullscreen is now Ctrl/Cmd+Shift+F since we mapped Cmd/Ctrl+F to search
- Fixed a issue where the video rendering could be held up by activity on the main thread. Should remove some of the stuttering under certain cirumstances
- Re-center the UI in the window on non 16:9 aspects
- Fixed an issue where the playback could start paused
- Fixed CEC input regression

* Sat Mar 26 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.6-2
- Fixes desktop file syntax.

* Sat Mar 26 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.6-1
- New upstream version 1.0.6.229.
- Workaround added for issue #244.
- Search! There is now global search in PMP. It's early days and doesn't work well with keyboards yet.
- The "three dots" indicating buffering could stick around for a very long time. We fixed that.
- MPEG-2 video direct playback is now working correctly.
- Switching servers from the dashboard is no longer slow.
- A variety of smaller fixes in the web-client.
- PMP will now open on the same physcial screen it was on last.
- Various resizing issues has been fixed where PMP could be stuck at very small size percentage.

* Wed Feb 24 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.5-1
- New upstream version 1.0.5.210.
- Updated web-client to 2.5.5. See https://forums.plex.tv/discussion/comment/1130675/#Comment_1130675 for details.
- Volume control: +/- is now mapped to volume control. Change your mapping to do increase/decrease_volume.
- Filter out the use of Num+ in the keymaps.
- Remove old update packages lying around on disk.
- Fix crash if we could not initialize Direct3D.
- The 7.1 audio OS X fixes described in 1.0.4 weren't actually shipped. Now they are.

* Tue Feb 02 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.4-1
- New upstream version 1.0.4.169.

* Sun Jan 03 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.3-7
- The "plexmediaplayer" user does not need a valid shell.

* Sun Jan 03 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.3-6
- Force permissions on /var/lib/plexmediaplayer.
- Adding SELinux rules for standalone mode.
- New script to enable standalone mode.

* Sun Jan 03 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.3-5
- Fixes user shell and home directory.
- Multiples fixes in Systemd files.

* Sun Jan 03 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.3-4
- Fixes user creation.

* Sun Jan 03 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.3-3
- Fixes standalone execution scripts.

* Sun Jan 03 2016 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.3-2
- Standalone execution support.
- Updated AppData XML.

* Tue Dec 29 2015 Jonathan Leroy <jonathan@harrycow.fr> - 1.0.3-1
- Plex Media Player version 1.0.3.

