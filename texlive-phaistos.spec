# revision 18651
# category Package
# catalog-ctan /fonts/archaic/phaistos
# catalog-date 2008-07-09 12:34:16 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-phaistos
Version:	1.0
Release:	1
Summary:	Disk of Phaistos font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/archaic/phaistos
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phaistos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phaistos.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phaistos.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A font that contains all the symbols of the famous Disc of
Phaistos, together with a LaTeX package. The disc was 'printed'
by stamping the wet clay with some sort of punches, probably
around 1700 BCE. The font is available in Adobe Type 1 and
OpenType formats (the latter using the Unicode positions for
the symbols). There are those who believe that this Cretan
script was used to 'write' Greek (it is known, for example,
that the rather later Cretan Linear B script was used to write
Greek), but arguments for other languages have been presented.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/phaistos/phaistos.afm
%{_texmfdistdir}/fonts/map/dvips/phaistos/phaistos.map
%{_texmfdistdir}/fonts/opentype/public/phaistos/Phaistos.otf
%{_texmfdistdir}/fonts/tfm/public/phaistos/phaistos.tfm
%{_texmfdistdir}/fonts/type1/public/phaistos/phaistos.pfb
%{_texmfdistdir}/tex/latex/phaistos/phaistos.sty
%doc %{_texmfdistdir}/doc/fonts/phaistos/getglyphs
%doc %{_texmfdistdir}/doc/fonts/phaistos/glyphTable.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/phaistos/phaistos.dtx
%doc %{_texmfdistdir}/source/fonts/phaistos/phaistos.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
