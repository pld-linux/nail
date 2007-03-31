Summary:	An enhanced implementation of the mailx command
Summary(pl.UTF-8):	Rozszerzona implementacja komendy mailx
Name:		nail
Version:	11.25
Release:	3
License:	BSD
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/nail/%{name}-%{version}.tar.bz2
# Source0-md5:	54f42db31911d734fcf37a89b72d4df7
Patch0:		%{name}-pure.patch
Patch1:		%{name}-bsdcompat.patch
URL:		http://nail.sourceforge.net/
BuildRequires:	krb5-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nail is derived from Berkeley Mail and is intended provide the
functionality of the POSIX mailx command with additional support
for MIME messages, IMAP, POP3, and SMTP. It provides enhanced
features for interactive use, such as caching and disconnected
operation for IMAP, message threading, scoring, and filtering.
It is also usable as a mail batch language, both for sending
and receiving mail.

%description -l pl.UTF-8
Nail został stworzony na podstawie Berkeley Mail z zamysłem
dostarczenia funkcjonalnosci komendy POSIX mailx z dodatkowym
wsparciem dla MIME, IMAP, POP3 i SMTP. Nail dostacza rozszerzone
możliwości przy pracy interaktywnej, takie jak odłączone operacje dla
IMAP, wątkowanie wiadomości, punktacja i filtrowanie.

%package mail
Summary:	A new /bin/mail - the "traditional" way to mail
Summary(pl.UTF-8):	Nowy /bin/mail - "tradycyjny" sposób wysyłania poczty
Group:		Applications/Mail
Obsoletes:	mailx

%description mail
The /bin/mail program can be used to send quick mail messages, and is
often used in shell scripts.

%description mail -l de.UTF-8
Das /bin/mail-Programm dient zum Versenden von Quick-Mail- Nachrichten
und wird häufig in Shell-Skripts verwendet.

%description mail -l fr.UTF-8
Le programme /bin/mail peut être utilisé pour envoyer des mails
rapides et est souvent utilisé dans les scripts shell.

%description mail -l pl.UTF-8
Przy pomocy programu /bin/mail można wysyłać pocztę. Często jest on
wykorzystywany w skryptach powłoki.

%description mail -l tr.UTF-8
/bin/mail programı hızlı olarak mektup göndermek için kullanılabilir.
Genellikle kabuk yorumlayıcıları içinde kullanılır.

%prep
%setup -q
cp makeconfig makeconfig-pure
%patch0 -p1
%patch1 -p1
chmod 755 makeconfig*

%build
./makeconfig-pure

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	MAILRC=/etc/mail.rc \
	MAILSPOOL=/var/mail \
	SENDMAIL=/usr/lib/sendmail

mv nail mail

./makeconfig

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	MAILRC=/etc/nail.rc \
	MAILSPOOL=/var/mail \
	SENDMAIL=/usr/lib/sendmail

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/skel,/bin}

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	UCBINSTALL=/usr/bin/install \
	PREFIX=%{_prefix} \

install mail $RPM_BUILD_ROOT/bin/mail

install nail.rc $RPM_BUILD_ROOT/etc/skel/.mailrc
install nail.rc $RPM_BUILD_ROOT/etc/mail.rc

ln -sf ../../bin/mail $RPM_BUILD_ROOT%{_bindir}/Mail
ln -sf nail $RPM_BUILD_ROOT%{_bindir}/mailx

install nail.1 $RPM_BUILD_ROOT%{_mandir}/man1/mail.1
echo .so mail.1 > $RPM_BUILD_ROOT%{_mandir}/man1/mailx.1
echo .so mail.1 > $RPM_BUILD_ROOT%{_mandir}/man1/Mail.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%config(noreplace) %verify(not md5 mtime size) /etc/nail.rc
%attr(755,root,root) %{_bindir}/nail
%attr(755,root,root) %{_bindir}/mailx
%{_mandir}/man1/n*
%{_mandir}/man1/mailx*

%files mail
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%config(noreplace) %verify(not md5 mtime size) /etc/mail.rc

/etc/skel/.mailrc

%attr(755,root,root) /bin/mail
%attr(755,root,root) %{_bindir}/Mail
%{_mandir}/man1/[Mm]ail.*
