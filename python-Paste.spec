Summary:	Tools for using a Web Server Gateway Interface stack
Summary(pl):	Narzêdzia do u¿ywania stosu Web Server Gateway Interface
Name:		python-Paste
Version:	0.4.1
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/P/Paste/Paste-%{version}.tar.gz
# Source0-md5:	955e04ebc3277cd37cc2b249f0a38b7f
URL:		http://pythonpaste.org/
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These provide several pieces of "middleware" (or filters) that can be
nested to build web applications. Each piece of middleware uses the
WSGI (PEP 333) interface, and should be compatible with other
middleware based on those interfaces.

%description -l pl
Ten pakiet dostarcza kilka czê¶ci "warstwy po¶redniej" (lub filtrów),
które mo¿na osadzaæ w celu zbudowania aplikacji WWW. Ka¿da czê¶æ
warstwy po¶redniej u¿ywa interfejsu WSGI (PEP 333) i powinna byæ
kompatybilna z inn± warstw± po¶redni± opart± na tych interfejsach.

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
