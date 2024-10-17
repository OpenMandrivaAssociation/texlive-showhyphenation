Name:		texlive-showhyphenation
Version:	67602
Release:	1
Summary:	Marking of hyphenation points
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/showhyphenation
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showhyphenation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showhyphenation.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package shows the hyphenation points in the document by
either inserting small triangles below the baseline or by
typesetting explicit hyphens. The markers are correctly placed
even within ligatures and their size adjusts to the font size.
By option the markers can be placed behind or in front of the
glyphs. The package requires LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/showhyphenation
%doc %{_texmfdistdir}/doc/lualatex/showhyphenation

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
