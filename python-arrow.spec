%define module arrow

Name:		python-arrow
Version:	1.4.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Better dates & times for Python
URL:		https://pypi.org/project/arrow/
License:	None
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Better dates & times for Python

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
