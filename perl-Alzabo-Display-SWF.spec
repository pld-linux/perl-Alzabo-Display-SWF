#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Alzabo
%define	pnam	Display-SWF
Summary:	Create SWF (Flash) Movies for visualizing Alzabo database schemas
#Summary(pl):	
Name:		perl-Alzabo-Display-SWF
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	380e05fd0287865310e742756d2a2688
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Alzabo   >= 0.72
BuildRequires:	perl-GraphViz >= 1.6
BuildRequires:	perl-ming
BuildRequires:	perl-YAML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Module uses the information provided by an Alzabo database schema
and - with the help of the GraphViz module and the Ming library -
creates a SWF Movie which contains a visualization of the data model.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes etc/[cm]*
%{perl_vendorlib}/%{pdir}/*/*
%{_mandir}/man3/*
