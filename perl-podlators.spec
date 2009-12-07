%define upstream_name    podlators
%define upstream_version 2.2.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Convert POD data to formatted ASCII text
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(File::Spec)
BuildRequires: perl(Pod::Simple)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/pod2man
/usr/bin/pod2text
/usr/share/man/man1/pod2man.1.lzma
/usr/share/man/man1/pod2text.1.lzma

