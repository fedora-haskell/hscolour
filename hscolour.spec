# cabal2spec-0.25.2
# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

%global pkg_name hscolour

# use following to bootstrap after building a new ghc version:
#%%{?ghc_bootstrap}
#%%global ghc_bootstrapping 1
#%%global without_hscolour 1

%global common_summary Haskell %{pkg_name} library

%global common_description hscolour is a tool to colourize Haskell code.\
It currently has six output formats: ANSI terminal codes, HTML 3.2\
with <font> tags, HTML 4.01 with CSS, XHTML 1.0 with inline CSS\
styling, LaTeX, and mIRC chat client codes.

Name:           %{pkg_name}
Version:        1.19
Release:        6%{?dist}
Summary:        Colourizes Haskell code

Group:          Development/Tools
License:        GPLv2+
# BEGIN cabal2spec
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ghc_arches}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros %{!?without_hscolour:hscolour}
# END cabal2spec

%description
%{common_description}


%prep
%setup -q


%build
%ghc_lib_build


%install
%ghc_lib_install


# library subpackage
%ghc_package

%ghc_description


# devel subpackage
%ghc_devel_package

%ghc_devel_description


%ghc_devel_post_postun


%files
%doc LICENCE-GPL
%attr(755,root,root) %{_bindir}/HsColour
%{_datadir}/%{name}-%{version}


%ghc_files LICENCE-GPL


%changelog
* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 1.19-6
- normal full build

* Wed Mar 21 2012 Jens Petersen <petersen@redhat.com> - 1.19-5
- bootstrap build
- drop the explicit containers BR

* Mon Jan 23 2012 Jens Petersen <petersen@redhat.com> - 1.19-4
- update to cabal2spec-0.25.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.19-2.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 1.19-2.1
- rebuild with new gmp

* Fri Jun 17 2011 Jens Petersen <petersen@redhat.com> - 1.19-2
- use ghc_arches (cabal-0.23.2)

* Fri Jun 17 2011 Jens Petersen <petersen@redhat.com> - 1.19-1
- update to 1.19
- use ghc_bootstrap from ghc-rpm-macros-0.13.5
- just depends on containers

* Thu May 05 2011 Jiri Skala <jskala@redhat.com> - 1.17-10
- enable source hscolour again

* Tue May 03 2011 Jiri Skala <jskala@redhat.com> - 1.17-9
- temporily disable hscolour for ghc-7.0.2 bootstrap on ppc64

* Thu Mar 10 2011 Jens Petersen <petersen@redhat.com> - 1.17-8
- enable source hscolour again

* Thu Mar 10 2011 Jens Petersen <petersen@redhat.com> - 1.17-7
- temporily disable hscolour for ghc-7.0.2 bootstrap

* Wed Feb 23 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.17-6
- enable build on sparcv9

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
