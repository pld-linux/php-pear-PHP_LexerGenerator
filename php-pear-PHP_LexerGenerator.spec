%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	LexerGenerator
%define		_status		alpha
%define		_pearname	PHP_LexerGenerator
Summary:	%{_pearname} - translate lexer files in lex2php format into a PHP 5 lexer
Summary(pl.UTF-8):	%{_pearname} - tłumaczenie plików leksera z formatu lex2php do leksera PHP 5
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e4c26822a30854ac30022f0679b6f66f
URL:		http://pear.php.net/package/PHP_LexerGenerator/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Translate a lexer file with a format similar to re2c
(http://re2c.org/) into a PHP 5 lexer for use with a parser.

Unlike re2c (as of re2c version 0.11), generated lexers are
state-aware out of the box.

Generated lexers are very efficient, more than twice as efficient as
other alternatives like csLex (written in C#) because they utilize
PHP's built-in Perl-compatible regular expressions to lex for tokens.

Now in version 0.3.0+, with processing instruction %%longestmatch,
generated lexers will always pick the longest string to match, rather
than the first. Generated lexers are slightly slower, but match
behavior of legacy lexers like flex, lex, re2c.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten umożliwia tłumaczenie plików leksera formatu zbliżonego do
re2c (http://re2c.org/) do formatu leksera PHP 5.

W odróżnieniu od re2c (w wersji 0.11), wygenerowane leksery domyślnie
są świadome stanu.

Wygenerowane lekery są bardzo wydajne, co najmniej dwa razy bardziej
niż alternatywy takie jak csLex (napisany w C#), ponieważ wykorzystują
wbudowany w PHP silnik wyrażeń regularnych w celu dopasowywania
tokenów.

Od wersji 0.3.0, korzystając z instrukcji %%longestmatch wygenerowane
leksery będą zawsze wybierały najdłuższy pasujący łańcuch znaków,
zamiast pierwszego. Wygenerowane tokeny będą odrobinę wolniejsze, ale
zachowywać się będą w sposób zbliżony do klasycznych lekserów takich
jak flex, lex, re2c.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install ./%{_bindir}/plex $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/PHP_LexerGenerator/examples
%attr(755,root,root) %{_bindir}/plex
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PHP/LexerGenerator
%{php_pear_dir}/PHP/LexerGenerator.php
%{php_pear_dir}/data/PHP_LexerGenerator

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/PHP_LexerGenerator
