Summary:	A new /bin/mail - the "traditional" way to mail
Summary(pl):	Nowy /bin/mail - "tradycyjny" sposób wysy³ania poczty
Name:		nail
Version:	11.22
Release:	1
License:	BSD
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/nail/%{name}-%{version}.tar.bz2
# Source0-md5:	caad4c4cd02c7fbf0d9e7fec50ff3b21
URL:		http://nail.sourceforge.net/
BuildRequires:	heimdal-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The /bin/mail program can be used to send quick mail messages, and is
often used in shell scripts.

%description -l de
Das /bin/mail-Programm dient zum Versenden von Quick-Mail- Nachrichten
und wird häufig in Shell-Skripts verwendet.

%description -l fr
Le programme /bin/mail peut être utilisé pour envoyer des mails
rapides et est souvent utilisé dans les scripts shell.

%description -l pl
Przy pomocy programu /bin/mail mo¿na wysy³aæ pocztê. Czêsto jest on
wykorzystywany w skryptach pow³oki.

%description -l tr
/bin/mail programý hýzlý olarak mektup göndermek için kullanýlabilir.
Genellikle kabuk yorumlayýcýlarý içinde kullanýlýr.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	UCBINSTALL=/usr/bin/install \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%config(noreplace) %verify(not md5 mtime size) /etc/nail.rc
%attr(755,root,root) %{_bindir}/nail
%{_mandir}/man1/*
