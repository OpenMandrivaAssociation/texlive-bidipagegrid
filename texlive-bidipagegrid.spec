%global tl_name bidipagegrid
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Bidi-aware page grid in background
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/bidipagegrid
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidipagegrid.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidipagegrid.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is based on pagegrid.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/xelatex
%dir %{_datadir}/texmf-dist/tex/xelatex
%dir %{_datadir}/texmf-dist/doc/xelatex/bidipagegrid
%dir %{_datadir}/texmf-dist/tex/xelatex/bidipagegrid
%doc %{_datadir}/texmf-dist/doc/xelatex/bidipagegrid/README
%doc %{_datadir}/texmf-dist/doc/xelatex/bidipagegrid/bidipagegrid-doc.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidipagegrid/bidipagegrid-doc.tex
%{_datadir}/texmf-dist/tex/xelatex/bidipagegrid/bidipagegrid.sty
