Name:		texlive-phaistos
Version:	18651
Release:	2
Summary:	Disk of Phaistos font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/archaic/phaistos
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phaistos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phaistos.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phaistos.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
