Summary:	Tools for using a Web Server Gateway Interface stack
Summary(pl):	Narz�dzia do u�ywania stosu Web Server Gateway Interface
Name:		python-Paste
Version:	1.0
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/P/Paste/Paste-%{version}.tar.gz
# Source0-md5:	d000bba7779d8540e3a1d18bce452cc9
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

%description -l pl
Ten pakiet dostarcza kilka cz�ci "warstwy po�redniej" (lub filtr�w),
kt�re mo�na osadza� w celu zbudowania aplikacji WWW. Ka�da cz��
warstwy po�redniej u�ywa interfejsu WSGI (PEP 333) i powinna by�
kompatybilna z inn� warstw� po�redni� opart� na tych interfejsach.

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
