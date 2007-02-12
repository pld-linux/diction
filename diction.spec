Summary:	Analyze text for style
Summary(pl.UTF-8):   Narzędzie analizujące tekst pod kątem stylu
Name:		diction
Version:	1.09
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://www.moria.de/~michael/diction/%{name}-%{version}.tar.gz
# Source0-md5:	eb82a90bbc93141f10deed301902d160
Patch1:		%{name}-texi.patch
URL:		http://www.moria.de/~michael/diction/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU diction and style are free implementations of old standard unix
commands, that are not available on many modern systems, because they
have been unbundled. Diction prints wordy and commonly misused
phrases. Style analyses surface characteristics of a document, e.g.
sentence length and various readability measures, but unlike the
original code, it lacks sentence type, word usage and most sentence
beginning processing.

Both commands support English and German documents.

%description -l pl.UTF-8
GNU diction oraz style są otwartymi implementacjami starych,
standardowych komend uniksowych, które nie są dostępne na wielu
nowoczesnych systemach. Diction wypisuje częste pomyłki słowne i źle
użyte wyrażenia. Style analizuje powierzchniowe charakterystyki
dokumentu, np. długość zdań oraz różne wskaźniki czytelności, jednak w
przeciwieństwie do oryginalnej wersji nie przeprowadza analizy typu
zdań, użycia słów oraz początków zdań.

Obie komendy wspierają języki angielski i niemiecki.

%prep
%setup -q
%patch1 -p1

%build
%{__autoconf}
cp -f %{_datadir}/automake/{config.*,missing} .
%configure
%{__make}
makeinfo diction.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install diction*.info $RPM_BUILD_ROOT%{_infodir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_infodir}/*.info*
