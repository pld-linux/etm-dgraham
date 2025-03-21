Summary:	Event and task manager
Name:		etm-dgraham
Version:	5.1.12
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	https://files.pythonhosted.org/packages/source/e/etm-dgraham/%{name}-%{version}.tar.gz
# Source0-md5:	8963d19c28e058db5b666d94be514b04
URL:		https://dagraham.github.io/etm-dgraham/
BuildRequires:	python3 >= 1:3.7.3
BuildRequires:	python3-modules >= 1:3.7.3
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7.3
Requires:	python3-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminal based event and task manager with goal to be the Swiss Army
Knife of tools for managing reminders.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/etm
%attr(755,root,root) %{_bindir}/etm+
%{py3_sitescriptdir}/etm
%{py3_sitescriptdir}/etm_dgraham-*-py*.egg-info
