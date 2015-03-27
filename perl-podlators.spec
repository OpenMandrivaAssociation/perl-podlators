%define upstream_name    podlators
%define upstream_version 2.5.3

Summary:	Convert POD data to formatted ASCII text
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Pod::Simple)
BuildArch:	noarch

%description
Pod::Man is a module to convert documentation in the POD format (the
preferred language for documenting Perl) into *roff input using the man
macro set. The resulting *roff code is suitable for display on a terminal
using the nroff(1) manpage, normally via the man(1) manpage, or printing
using the troff(1) manpage. It is conventionally invoked using the driver
script *pod2man*, but it can also be used directly.

As a derived class from Pod::Simple, Pod::Man supports the same methods and
interfaces. See the Pod::Simple manpage for all the details.

new() can take options, in the form of key/value pairs that control the
behavior of the parser. See below for details.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_bindir}/pod2man
%{_bindir}/pod2text
%{_mandir}/man1/*
%{_mandir}/man3/*
