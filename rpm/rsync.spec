Name:       rsync
Summary:    A program for synchronizing files over a network
Version:    3.4.0
Release:    1
License:    GPLv3+
URL:        https://github.com/sailfishos/rsync
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(liblz4)
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

%prep
%autosetup -n %{name}-%{version}/upstream

%build

%configure \
  --disable-md2man \
  --disable-xxhash

%make_build

%install

%make_install
mkdir -p %{buildroot}/etc/xinetd.d
install -m 644 packaging/lsb/rsync.xinetd %{buildroot}/etc/xinetd.d/rsync

%files
%license COPYING
%config(noreplace) /etc/xinetd.d/rsync
%{_bindir}/rsync
%{_bindir}/rsync-ssl
