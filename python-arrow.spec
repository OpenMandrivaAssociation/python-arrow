Name:		python-arrow
Version:	1.3.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/arrow/arrow-%{version}.tar.gz
Summary:	Better dates & times for Python
URL:		https://pypi.org/project/arrow/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Better dates & times for Python

%files
%{py_sitedir}/arrow
%{py_sitedir}/arrow-*.*-info
