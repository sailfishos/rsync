Name:       rsync
Summary:    A program for synchronizing files over a network
Version:    3.1.3
Release:    1
License:    GPLv3+
URL:        https://github.com/sailfishos/rsync
Source0:    %{name}-%{version}.tar.gz
Obsoletes:  rsync-support
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

%package doc
Summary:   Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build

%configure
make %{_smp_mflags}

%install
rm -rf %{buildroot}

%make_install
mkdir -p %{buildroot}/etc/xinetd.d
install -m 644 packaging/lsb/rsync.xinetd %{buildroot}/etc/xinetd.d/rsync

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version}/ README

%files
%defattr(-,root,root,-)
%license COPYING
%config(noreplace) /etc/xinetd.d/rsync
%{_bindir}/rsync

%files doc
%doc %{_docdir}/%{name}-%{version}
