Summary:	An enhanced implementation of the mailx command
Summary(pl):	Rozszerzona implementacja komendy mailx
Name:		nail
Version:	11.22
Release:	2
License:	BSD
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/nail/%{name}-%{version}.tar.bz2
# Source0-md5:	caad4c4cd02c7fbf0d9e7fec50ff3b21
Patch0:		%{name}-pure.patch
Patch1:		%{name}-bsdcompat.patch
URL:		http://nail.sourceforge.net/
BuildRequires:	heimdal-devel
BuildRequires:	openssl-devel >= 0.9.7d
Requires:	%{name}-mail = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nail is derived from Berkeley Mail and is intended provide the
functionality of the POSIX mailx command with additional support
for MIME messages, IMAP, POP3, and SMTP. It provides enhanced
features for interactive use, such as caching and disconnected
operation for IMAP, message threading, scoring, and filtering.
It is also usable as a mail batch language, both for sending
and receiving mail.

%description -l pl
Nail zosta³ stworzony na podstawie Berkeley Mail z zamys³em
dostarczenia funkcjonalnosci komendy POSIX mailx z dodatkowym
wsparciem dla MIME, IMAP, POP3 i SMTP. Nail dostacza rozszerzone
mo¿liwo¶ci przy pracy interaktywnej, jak od³±czon± pracê dla IMAP,
w±tkowanie wiadomo¶ci, punktacja i filtrowanie.

%package mail
Summary:	A new /bin/mail - the "traditional" way to mail
Summary(pl):	Nowy /bin/mail - "tradycyjny" sposób wysy³ania poczty
Group:		Applications/Mail

%description mail
The /bin/mail program can be used to send quick mail messages, and is
often used in shell scripts.

%description mail -l de
Das /bin/mail-Programm dient zum Versenden von Quick-Mail- Nachrichten
und wird häufig in Shell-Skripts verwendet.

%description mail -l fr
Le programme /bin/mail peut être utilisé pour envoyer des mails
rapides et est souvent utilisé dans les scripts shell.

%description mail -l pl
Przy pomocy programu /bin/mail mo¿na wysy³aæ pocztê. Czêsto jest on
wykorzystywany w skryptach pow³oki.

%description mail -l tr
/bin/mail programý hýzlý olarak mektup göndermek için kullanýlabilir.
Genellikle kabuk yorumlayýcýlarý içinde kullanýlýr.

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
