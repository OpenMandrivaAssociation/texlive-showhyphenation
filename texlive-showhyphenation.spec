%global tl_name showhyphenation
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Marking of hyphenation points
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/showhyphenation
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showhyphenation.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showhyphenation.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package shows the hyphenation points in the document by either
inserting small triangles below the baseline or by typesetting explicit
hyphens. The markers are correctly placed even within ligatures and
their size adjusts to the font size. By option the markers can be placed
behind or in front of the glyphs. The package requires LuaLaTeX.

