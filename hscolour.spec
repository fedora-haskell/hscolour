# Updated to cabal2spec-0.22.2 and ghc-rpm-macros-0.8.1

%global pkg_name hscolour

%global common_summary Haskell %{pkg_name} library

%global common_description hscolour is a small Haskell package to colourize Haskell code.\
It currently has five output formats: ANSI terminal codes,\
HTML 3.2 with font tags, HTML 4.01 with CSS, LaTeX, and mIRC chat codes.

# debuginfo is not useful for ghc
%global debug_package %{nil}

Name:           %{pkg_name}
Version:        1.17
Release:        5%{?dist}
Summary:        Colourizes Haskell code

Group:          Development/Tools
License:        GPLv2+
URL:            http://www.cs.york.ac.uk/fp/darcs/hscolour/
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
# fedora ghc archs:
ExclusiveArch:  %{ix86} x86_64 ppc alpha
BuildRequires:  ghc, ghc-doc, ghc-prof
BuildRequires:  ghc-rpm-macros >= 0.7.3
BuildRequires:  hscolour
%{?ghc_pkg_deps:BuildRequires:  %{ghc_pkg_deps}, %(echo %{ghc_pkg_deps} | sed -e "s/\(ghc-[^, ]\+\)-devel/\1-doc,\1-prof/g")}

%description
%{common_description}

%files
%defattr(-,root,root,-)
%doc LICENCE-GPL
%attr(755,root,root) %{_bindir}/HsColour
%{_datadir}/%{name}-%{version}


%prep
%setup -q


%build
%ghc_lib_build


%install
%ghc_lib_install


%ghc_binlib_package


%changelog
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jens Petersen <petersen@redhat.com> - 1.17-4
- rebuild

* Sat Jan 15 2011 Jens Petersen <petersen@redhat.com> - 1.17-3
- update to cabal2spec-0.22.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 1.17-2
- rebuilt

* Mon Jul 19 2010 Jens Petersen <petersen@redhat.com> - 1.17-1
- 1.17 release
- use ghc-rpm-macros-0.8.1 macros: update to cabal2spec-0.22.1
- add hscolour and obsolete doc subpackage

* Sat Jun 26 2010 Jens Petersen <petersen@redhat.com> - 1.16-3
- strip dynlinked files (cabal2spec-0.21.4)

* Mon Feb 15 2010 Conrad Meyer <konrad@tylerc.org> - 1.16-1
- Bump to 1.16

* Mon Jan 11 2010 Jens Petersen <petersen@redhat.com> - 1.15-4
- update to ghc-rpm-macros-0.5.1 and cabal2spec-0.21.1:
- drop doc and prof bcond
- use common summary and common_description
- define pkg_name and use ghc_binlib_package

* Wed Dec 23 2009 Jens Petersen <petersen@redhat.com> - 1.15-3
- devel package requires shared library not base

* Wed Dec 23 2009 Jens Petersen <petersen@redhat.com> - 1.15-2
- update spec for ghc-6.12.1
- added shared library support: needs ghc-rpm-macros 0.3.1

* Fri Sep 18 2009 Jens Petersen <petersen@redhat.com> - 1.15-1
- update to 1.15

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Jens Petersen <petersen@redhat.com> - 1.13-1
- update to 1.13
- buildrequires ghc-rpm-macros (cabal2spec-0.16)

* Sat Apr 25 2009 Jens Petersen <petersen@redhat.com> - 1.12-3
- sync with cabal2spec-0.15

* Tue Mar 10 2009 Jens Petersen <petersen@redhat.com> - 1.12-2
- fix url (#488665)
- fix HsColour permissions (#488665)

* Thu Mar  5 2009 Jens Petersen <petersen@redhat.com> - 1.12-1
- initial packaging for Fedora created by cabal2spec
