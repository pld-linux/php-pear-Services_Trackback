# TODO
#  - fix pl summary/description

%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Trackback
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - a generic class for sending and receiving trackbacks
Summary(pl.UTF-8):	%{_pearname} - podstawowa klasa do wysyłania i odbierania trackbacków
Name:		php-pear-%{_pearname}
Version:	0.6.2
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a59cfa706b47468dff510c78cd1b9dbe
URL:		http://pear.php.net/package/Services_Trackback/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.2.4
Requires:	php-pear-Net_DNSBL
Requires:	php-pear-Var_Dump
Obsoletes:	php-pear-Services_Trackback-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A generic class for sending and receiving trackbacks.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Podstawowa klasa do wysyłania i odbierania trackbacków.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
