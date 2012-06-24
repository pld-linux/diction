Summary:	Analyze text for style
Summary(pl):	Narz�dzie analizuj�ce tekst pod k�tem stylu
Name:		diction
Version:	1.08
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://www.moria.de/~michael/diction/%{name}-%{version}.tar.gz
# Source0-md5:	baf3d7ada45c67a269035377a9c9ba3a
Patch1:		%{name}-texi.patch
URL:		http://www.moria.de/~michael/diction/
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl
GNU diction oraz style s� otwartymi implementacjami starych,
standardowych komend uniksowych, kt�re nie s� dost�pne na wielu
nowoczesnych systemach. Diction wypisuje cz�ste pomy�ki s�owne i �le
u�yte wyra�enia. Style analizuje powierzchniowe charakterystyki
dokumentu, np. d�ugo�� zda� oraz r�ne wska�niki czytelno�ci, jednak w
przeciwie�stwie do oryginalnej wersji nie przeprowadza analizy typu
zda�, u�ycia s��w oraz pocz�tk�w zda�.

Obie komendy wspieraj� j�zyki angielski i niemiecki.

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
