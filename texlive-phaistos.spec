%global tl_name phaistos
%global tl_revision 79618
%global tl_version 1.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Disk of Phaistos font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/archaic/phaistos
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phaistos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phaistos.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phaistos.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
A font that contains all the symbols of the famous Disc of Phaistos,
together with a LaTeX package. The disc was 'printed' by stamping the
wet clay with some sort of punches, probably around 1700 BCE. The font
is available in Adobe Type 1 and OpenType formats (the latter using the
Unicode positions for the symbols). There are those who believe that
this Cretan script was used to 'write' Greek (it is known, for example,
that the rather later Cretan Linear B script was used to write Greek),
but arguments for other languages have been presented.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from phaistos:
Map phaistos.map
TL_DROPIN_EOF
