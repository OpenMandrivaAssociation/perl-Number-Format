%define upstream_name    Number-Format
%define upstream_version 1.73

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Convert numbers to strings with pretty formatting
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Number/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Number::Format is a library for formatting numbers.  Functions are
provided for converting numbers to strings in a variety of ways, and to
convert strings that contain numbers back into numeric form.  The output
formats may include thousands separators - characters inserted between
each group of three characters counting right to left from the decimal
point.  The characters used for the decimal point and the thousands
separator come from the locale information or can be specified by the
user.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 CHANGES README

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/Number
%{_mandir}/*/*

%changelog
* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.730.0-1mdv2010.0
+ Revision: 449778
- update to 1.73

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.720.0-1mdv2010.0
+ Revision: 404280
- rebuild using %%perl_convert_version

* Wed May 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.72-1mdv2010.0
+ Revision: 372391
- update to new version 1.72

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.71-1mdv2010.0
+ Revision: 371868
- new version

* Sun Feb 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.70-1mdv2009.1
+ Revision: 340536
- update to new version 1.70

* Thu Feb 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.63-1mdv2009.1
+ Revision: 339908
- update to new version 1.63

* Tue Feb 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.62-1mdv2009.1
+ Revision: 339103
- update to new version 1.62

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.52-5mdv2009.0
+ Revision: 258142
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.52-4mdv2009.0
+ Revision: 246255
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.52-2mdv2008.1
+ Revision: 133639
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Sep 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.52-1mdv2007.0
- New version 1.52

* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.45-2mdv2007.0
- Rebuild

* Tue Apr 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.45-1mdk
- Contributed by Cedric Devillers <brancaleone@altern.org>

