#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Tools for using a Web Server Gateway Interface stack
Summary(pl.UTF-8):	Narzędzia do używania stosu Web Server Gateway Interface
Name:		python-Paste
# keep 2.x / < 3.7 here for python2 support
Version:	2.0.3
Release:	10
Group:		Libraries/Python
License:	MIT
#Source0Download: https://pypi.org/simple/paste/
Source0:	https://files.pythonhosted.org/packages/source/P/Paste/Paste-%{version}.tar.gz
# Source0-md5:	1231e14eae62fa7ed76e9130b04bc61e
Patch0:		%{name}-py3.7.patch
URL:		https://pypi.org/project/Paste/
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%if %{with tests}
BuildRequires:	python-nose >= 0.11
BuildRequires:	python-six >= 1.13.0
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Paste provides several pieces of "middleware" (or filters) that can be
nested to build web applications. Each piece of middleware uses the
WSGI (PEP 333) interface, and should be compatible with other
middleware based on those interfaces.

%description -l pl.UTF-8
Pakiet Paste dostarcza kilka części warstwy pośredniej (lub filtrów),
które można osadzać w celu zbudowania aplikacji WWW. Każda część
warstwy pośredniej używa interfejsu WSGI (PEP 333) i powinna być
kompatybilna z inną warstwą pośrednią opartą na tych interfejsach.

%package -n python3-Paste
Summary:	Tools for using a Web Server Gateway Interface stack
Summary(pl.UTF-8):	Narzędzia do używania stosu Web Server Gateway Interface
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-Paste
Paste provides several pieces of "middleware" (or filters) that can be
nested to build web applications. Each piece of middleware uses the
WSGI (PEP 333) interface, and should be compatible with other
middleware based on those interfaces.

%description -n python3-Paste -l pl.UTF-8
Pakiet Paste dostarcza kilka części warstwy pośredniej (lub filtrów),
które można osadzać w celu zbudowania aplikacji WWW. Każda część
warstwy pośredniej używa interfejsu WSGI (PEP 333) i powinna być
kompatybilna z inną warstwą pośrednią opartą na tych interfejsach.

%package apidocs
Summary:	API documentation for Python Paste module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona Paste
Group:		Documentation

%description apidocs
API documentation for Python Paste module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona Paste.

%prep
%setup -q -n Paste-%{version}
%patch -P 0 -p1

# junk in archive
%{__rm} paste/*.py.orig paste/util/*.py.orig
# online test + requires outdated pythonpaste.org website content
%{__rm} tests/test_proxy.py

%build
%py_build %{?with_tests:test}

%if %{with doc}
sphinx-build-2 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst docs/{license,news}.txt
# paste is also top dir for other python-Paste* packages
%dir %{py_sitescriptdir}/paste
%{py_sitescriptdir}/paste/auth
%{py_sitescriptdir}/paste/cowbell
%{py_sitescriptdir}/paste/debug
%{py_sitescriptdir}/paste/evalexception
%{py_sitescriptdir}/paste/exceptions
%{py_sitescriptdir}/paste/util
%{py_sitescriptdir}/paste/*.py[co]
%{py_sitescriptdir}/Paste-%{version}-py*.egg-info
%{py_sitescriptdir}/Paste-%{version}-py*-nspkg.pth

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,community,download,include,modules,*.html,*.js}
%endif
