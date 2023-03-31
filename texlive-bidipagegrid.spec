Name:		texlive-bidipagegrid
Version:	34632
Release:	2
Summary:	Bidi-aware page grid in background
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bidipagegrid
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidipagegrid.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidipagegrid.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is based on pagegrid.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/bidipagegrid
%doc %{_texmfdistdir}/doc/xelatex/bidipagegrid

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
