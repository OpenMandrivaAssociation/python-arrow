%define module arrow

Name:		python-arrow
Version:	1.4.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Better dates & times for Python
URL:		https://pypi.org/project/arrow/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Better dates & times for Python

%prep -a
# flit 4 does not accept the upper bound, and the version is not a static assignment.
sed -i 's/flit_core >=3.2,<4/flit_core >=3.2/' pyproject.toml
sed -i 's/dynamic = \["version"\]/version = "%{version}"/' pyproject.toml

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
