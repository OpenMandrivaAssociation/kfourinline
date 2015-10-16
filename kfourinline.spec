Name:		kfourinline
Summary:	Place 4 pieces in a row
Version:	15.08.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kfourinline
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5KDEGames)
BuildRequires: 	cmake(ECM)

BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)

BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5KDELibs4Support)

%description
KFourInLine is a board game for two players based on the Connect-Four game.

The players try to build up a row of four pieces using different strategies.

%files
%{_bindir}/kfourinline
%{_bindir}/kfourinlineproc
%{_datadir}/applications/org.kde.kfourinline.desktop
%{_datadir}/kfourinline
%doc %{_docdir}/*/*/kfourinline
%{_iconsdir}/hicolor/*/apps/kfourinline.png
%{_datadir}/config.kcfg/kwin4.kcfg
%{_datadir}/kxmlgui5/kfourinline/kfourinlineui.rc

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
