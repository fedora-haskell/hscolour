%bcond_without doc
%bcond_without prof
%bcond_without shared

# ghc does not emit debug information
%global debug_package %{nil}

Name:           hscolour
Version:        1.15
Release:        2%{?dist}
Summary:        Colourizes Haskell code

Group:          Development/Tools
License:        GPLv2+
URL:            http://www.cs.york.ac.uk/fp/darcs/hscolour/
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
# fedora ghc archs:
ExclusiveArch:  %{ix86} x86_64 ppc alpha
BuildRequires:  ghc, ghc-rpm-macros >= 0.3.1
%if %{with doc}
BuildRequires:  ghc-doc
%endif
%if %{with prof}
BuildRequires:  ghc-prof
%endif

%description
hscolour is a small Haskell script to colourize Haskell code.
It currently has five output formats: ANSI terminal codes,
HTML 3.2 with font tags, HTML 4.01 with CSS, LaTeX, and mIRC chat codes.


%if %{with shared}
%package -n ghc-%{name}
Summary:        Haskell library for %{name}
Group:          System Environment/Libraries

%description -n ghc-%{name}
Haskell %{name} library for ghc.
%endif


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Group:          Development/Libraries
Requires:       ghc = %{ghc_version}
Requires(post): ghc = %{ghc_version}
Requires(postun): ghc = %{ghc_version}
%if %{with shared}
Requires:       %{name} = %{version}-%{release}
%endif

%description -n ghc-%{name}-devel
This package contains the development files for %{name}
built for ghc-%{ghc_version}.


%if %{with doc}
%package -n ghc-%{name}-doc
Summary:        Documentation for %{name}
Group:          Development/Libraries
Requires:       ghc-doc = %{ghc_version}
Requires(post): ghc-doc = %{ghc_version}
Requires(postun): ghc-doc = %{ghc_version}

%description -n ghc-%{name}-doc
This package contains development documentation files for the %{name} library.
%endif


%if %{with prof}
%package -n ghc-%{name}-prof
Summary:        Profiling libraries for %{name}
Group:          Development/Libraries
License:        LGPLv2+
Requires:       ghc-%{name}-devel = %{version}-%{release}
Requires:       ghc-prof = %{ghc_version}

%description -n ghc-%{name}-prof
This package contains profiling libraries for %{name}
built for ghc-%{ghc_version}.
%endif


%prep
%setup -q


%build
# dynamic + prof breaks cabal looking for p_dyn
%cabal_configure --ghc %{?with_prof:-p}
%cabal build
%if %{with doc}
%cabal haddock
%endif


%install
%cabal_install
%cabal_pkg_conf

%ghc_gen_filelists ghc-%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%post -n ghc-%{name}-devel
ghc-pkg recache


%if %{with doc}
%post -n ghc-%{name}-doc
%ghc_reindex_haddock
%endif


%preun -n ghc-%{name}-devel
ghc-pkg recache


%if %{with doc}
%postun -n ghc-%{name}-doc
if [ "$1" -eq 0 ] ; then
  %ghc_reindex_haddock
fi
%endif


%files
%defattr(-,root,root,-)
%doc README
%attr(755,root,root) %{_bindir}/HsColour
%{_datadir}/%{name}-%{version}


%if %{with shared}
%files -n ghc-%{name} -f ghc-%{name}.files
%defattr(-,root,root,-)
%doc LICENCE-GPL
%endif


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%defattr(-,root,root,-)
%if %{without shared}
%doc LICENCE-LGPL
%endif


%if %{with doc}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%defattr(-,root,root,-)
%endif


%if %{with prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%defattr(-,root,root,-)
%endif


%changelog
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
