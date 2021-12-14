Name:           deepin-music
Version:        5.0.1
Release:        4
Summary:        Deepin Music Player
Summary(zh_CN): 深度音乐播放器
License:        GPLv3
Url:            https://github.com/linuxdeepin/deepin-music
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  dtkcore2-devel
BuildRequires:  dtkwidget2-devel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(mpris-qt5)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  gcc
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
Requires:       deepin-desktop-base
Requires:       gstreamer1-plugins-good
Requires:       dbus

%description
Deepin Music Player with brilliant and tweakful UI Deepin-UI based,
gstreamer front-end, with features likes search music by pinyin,
quanpin, colorful lyrics supports, and more powerful functions
you will found.

%description -l zh_CN
深度音乐播放器界面基于 Deepin-UI , 后端使用 gstreamer ,
其他特性如音乐搜索, 丰富多彩的歌词支持, 更多功能等待您发现.

%prep
%autosetup
sed -i '/vendor/d' src/src.pro
sed -i '/%1/s|lib|%{_lib}|' src/music-player/core/pluginmanager.cpp
sed -i '/target.path/s|lib|%{_lib}|' src/libdmusic/libdmusic.pro \
    src/plugin/netease-meta-search/netease-meta-search.pro
sed -i 's|$$PWD/../vendor/mpris-qt/src|%{_qt5_includedir}/MprisQt/|g' src/music-player/build.pri
sed -i 's|$$PWD/../vendor/dbusextended-qt/src|%{_qt5_includedir}/DBusExtended|g' src/music-player/build.pri
rm src/vendor -rf

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -pDm644 %{S:1} %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
rm %{buildroot}/%{_datadir}/translations -rf

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/lib*.so.*
%{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dman/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml


%changelog
* Fir Dec 10 2021 weidong <weidong@uniontech.com> - 5.0.1-4
- Delete dist macro

* Tue Aug 03 2021 weidong <weidong@uniontech.com> - 5.0.1-3
- Init package
