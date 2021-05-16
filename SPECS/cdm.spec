Name:		cdm
Version:	master
Release:	1%{?dist}
Summary:	Console Display Manager
License:	GPL-2.0
URL:		https://github.com/evertiro/cdm
Source0:	%{URL}/archive/refs/heads/master.tar.gz

Requires:	bash

%description
The Console Display Manager

%prep
%autosetup

%install
install -d %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir} %{buildroot}%{_datadir}/doc/cdm/themes
install -Dm755 src/cdm src/cdm-xlaunch %{buildroot}%{_bindir}
install -Dm644 src/cdmrc %{buildroot}%{_sysconfdir}/cdmrc
install -Dm644 README.md src/profile.sh %{buildroot}%{_datadir}/doc/cdm
install -Dm644 themes/* %{buildroot}%{_datadir}/doc/cdm/themes

%files
%doc CHANGELOG.md
%{_bindir}/cdm
%{_bindir}/cdm-xlaunch
%config(noreplace) %{_sysconfdir}/cdmrc
%{_datadir}/doc/cdm/profile.sh
%{_datadir}/doc/cdm/README.md
%{_datadir}/doc/cdm/themes/blackandwhite
%{_datadir}/doc/cdm/themes/cdm
%{_datadir}/doc/cdm/themes/default
%{_datadir}/doc/cdm/themes/ed
%{_datadir}/doc/cdm/themes/elinks
%{_datadir}/doc/cdm/themes/haze
%{_datadir}/doc/cdm/themes/lime
