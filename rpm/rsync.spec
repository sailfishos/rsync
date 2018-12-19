Name:       rsync
Summary:    A program for synchronizing files over a network
Version: 3.1.0
Release: 1
Group:      Applications/Internet
License:    GPLv3+
URL:        http://rsync.samba.org/
Source0:    http://rsync.samba.org/ftp/rsync/src/rsync-%{version}.tar.gz
BuildRequires:  pkgconfig(popt)
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel

%description
Rsync uses a reliable algorithm to bring remote and host files into
sync very quickly. Rsync is fast because it just sends the differences
in the files over the network instead of sending the complete
files. Rsync is often used as a very powerful mirroring process or
just as a more capable replacement for the rcp command. A technical
report which describes the rsync algorithm is included in this
package.


%package support
Summary:    Support files for rsync
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}

%description support
Support files for rsync


%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires: %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build

%configure
make %{_smp_mflags}

%install
rm -rf %{buildroot}

# rename the pre-generated man pages
cp rsync.man rsync.1
cp rsyncd.conf.man rsyncd.conf.5

%make_install
mkdir -p %{buildroot}/etc/xinetd.d
install -m 644 packaging/lsb/rsync.xinetd %{buildroot}/etc/xinetd.d/rsync

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version}/ README

%files
%defattr(-,root,root,-)
%license COPYING
%config(noreplace) /etc/xinetd.d/rsync
%{_prefix}/bin/rsync

%files support
%defattr(-,root,root,-)

%files doc
%doc %{_docdir}/%{name}-%{version}
%doc %{_mandir}/man1/rsync.1*
%doc %{_mandir}/man5/rsyncd.conf.5*
