Name:		plasma6-kfourinline
Summary:	Place 4 pieces in a row
Version:	24.01.90
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kfourinline
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kfourinline-%{version}.tar.xz
BuildRequires:	cmake(KDEGames6)
BuildRequires: 	cmake(ECM)

BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)

BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DNSSD)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NotifyConfig)

%description
KFourInLine is a board game for two players based on the Connect-Four game.

The players try to build up a row of four pieces using different strategies.

%files -f kfourinline.lang
%{_datadir}/qlogging-categories6/kfourinline.categories
%{_datadir}/metainfo/org.kde.kfourinline.appdata.xml
%{_bindir}/kfourinline
%{_bindir}/kfourinlineproc
%{_datadir}/applications/org.kde.kfourinline.desktop
%{_datadir}/kfourinline
%{_iconsdir}/hicolor/*/apps/kfourinline.png
%{_datadir}/config.kcfg/kwin4.kcfg

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kfourinline-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kfourinline --with-html
