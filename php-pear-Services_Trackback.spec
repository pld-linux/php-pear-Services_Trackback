# TODO
#  - fix pl summary/description

%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Trackback
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a generic class for sending and receiving trackbacks
Summary(pl):	%{_pearname} - podstawowa klasa do wysy³ania i odbierania trackbacków
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	56ae320f9a32466c797ca15666748366
URL:		http://pear.php.net/package/Services_Trackback/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A generic class for sending and receiving trackbacks.

In PEAR status of this package is: %{_status}.

%description -l pl
Podstawowa klasa do wysy³ania i odbierania trackbacków.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/test
%{php_pear_dir}/%{_class}/*.php
