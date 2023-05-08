#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-LWP-UserAgent
Version  : 0.036
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-LWP-UserAgent-0.036.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-LWP-UserAgent-0.036.tar.gz
Summary  : 'A LWP::UserAgent suitable for simulating and testing network calls'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-LWP-UserAgent-license = %{version}-%{release}
Requires: perl-Test-LWP-UserAgent-perl = %{version}-%{release}
Requires: perl(HTTP::Date)
Requires: perl(HTTP::Request)
Requires: perl(HTTP::Response)
Requires: perl(HTTP::Status)
Requires: perl(LWP::UserAgent)
Requires: perl(Safe::Isa)
Requires: perl(Scalar::Util)
Requires: perl(Storable)
Requires: perl(Try::Tiny)
Requires: perl(URI)
Requires: perl(namespace::clean)
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Request::Common)
BuildRequires : perl(HTTP::Response)
BuildRequires : perl(HTTP::Status)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Safe::Isa)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Test::RequiresInternet)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)
BuildRequires : perl(namespace::clean)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Test-LWP-UserAgent,
version 0.036:
A LWP::UserAgent suitable for simulating and testing network calls

%package dev
Summary: dev components for the perl-Test-LWP-UserAgent package.
Group: Development
Provides: perl-Test-LWP-UserAgent-devel = %{version}-%{release}
Requires: perl-Test-LWP-UserAgent = %{version}-%{release}

%description dev
dev components for the perl-Test-LWP-UserAgent package.


%package license
Summary: license components for the perl-Test-LWP-UserAgent package.
Group: Default

%description license
license components for the perl-Test-LWP-UserAgent package.


%package perl
Summary: perl components for the perl-Test-LWP-UserAgent package.
Group: Default
Requires: perl-Test-LWP-UserAgent = %{version}-%{release}

%description perl
perl components for the perl-Test-LWP-UserAgent package.


%prep
%setup -q -n Test-LWP-UserAgent-0.036
cd %{_builddir}/Test-LWP-UserAgent-0.036

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-LWP-UserAgent
cp %{_builddir}/Test-LWP-UserAgent-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/perl-Test-LWP-UserAgent/05964c934352e268e785c27cc3f044860b43756b || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::LWP::UserAgent.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-LWP-UserAgent/05964c934352e268e785c27cc3f044860b43756b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
