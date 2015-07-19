Name:		kfourinline
Summary:	Place 4 pieces in a row
Version:	15.04.3
Release:	2
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kfourinline
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires: 	cmake(KF5NotifyConfig)
BuildRequires: 	cmake(ECM)

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