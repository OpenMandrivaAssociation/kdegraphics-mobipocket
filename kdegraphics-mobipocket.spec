Summary:	A collection of plugins to handle mobipocket files
Name:		kdegraphics-mobipocket
Version:	24.02.0
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	ninja
Conflicts:	kdegraphics4-core < 2:4.6.90
Obsoletes:	mobipocket < 2:4.8.0

%description
A collection of plugins to handle mobipocket files.

%files
%doc COPYING

#----------------------------------------------------------------------

%define major 2
%define libqmobipocket %mklibname qmobipocket %{major}

%package -n %{libqmobipocket}
Summary:	QMobipocket library
Group:		System/Libraries

%description -n %{libqmobipocket}
QMobipocket library.

%files -n %{libqmobipocket}
%{_libdir}/libqmobipocket.so.%{major}*

#----------------------------------------------------------------------

%define devqmobipocket %mklibname qmobipocket -d

%package -n %{devqmobipocket}
Summary:	Development files for QMobipocket
Group:		System/Libraries
Requires:	%{libqmobipocket} = %{EVRD}
Provides:	qmobipocket-devel = %{EVRD}

%description -n %{devqmobipocket}
Development files for QMobipocket.

%files -n %{devqmobipocket}
%{_includedir}/QMobipocket/
%{_libdir}/libqmobipocket.so
%{_libdir}/cmake/QMobipocket/

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
