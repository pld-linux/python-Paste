Summary:	Tools for using a Web Server Gateway Interface stack
Summary(pl.UTF-8):   Narzędzia do używania stosu Web Server Gateway Interface
Name:		python-Paste
Version:	1.1.1
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/P/Paste/Paste-%{version}.tar.gz
# Source0-md5:	6b6f05b34800e606b7f064724275ff87
URL:		http://pythonpaste.org/
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These provide several pieces of "middleware" (or filters) that can be
nested to build web applications. Each piece of middleware uses the
WSGI (PEP 333) interface, and should be compatible with other
middleware based on those interfaces.

%description -l pl.UTF-8
Ten pakiet dostarcza kilka części "warstwy pośredniej" (lub filtrów),
które można osadzać w celu zbudowania aplikacji WWW. Każda część
warstwy pośredniej używa interfejsu WSGI (PEP 333) i powinna być
kompatybilna z inną warstwą pośrednią opartą na tych interfejsach.

%prep
%setup -q -n Paste-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/
%{py_sitescriptdir}/paste*
%{py_sitescriptdir}/Paste*
