Name:       rsync
Summary:    A program for synchronizing files over a network
Version:    3.4.4
Release:    1
License:    GPLv3+
URL:        https://github.com/sailfishos/rsync
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel

%ifarch %ix86
BuildRequires:  python3-base
# Fix running chmod-symlink-race test with kernel 4.4 headers
Patch1:         0001-t_chmod_secure-probe-kernel-RESOLVE_BENEATH-at-runti.patch
Patch2:         0002-t_chmod_secure-use-HAVE_OPENAT2-to-check-for-openat2.patch
Patch3:         0003-android-probe-openat2-usability-behind-a-SIGSYS-hand.patch
# This test passes in OBS, but breaks in Platform SDK, optionally skip it.
Patch4:         0004-Skip-itemize-test-in-sb2.patch
%endif

%description
Rsync uses a reliable algorithm to bring remote and host files into
sync very quickly. Rsync is fast because it just sends the differences
in the files over the network instead of sending the complete
files. Rsync is often used as a very powerful mirroring process or
just as a more capable replacement for the rcp command. A technical
report which describes the rsync algorithm is included in this
package.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%configure \
  --disable-md2man
%make_build

%check
%ifarch %ix86
chmod +x support/*
%make_build -j1 check
chmod -x support/*
%endif

%install

%make_install
mkdir -p %{buildroot}/etc/xinetd.d
install -m 644 packaging/lsb/rsync.xinetd %{buildroot}/etc/xinetd.d/rsync

%files
%license COPYING
%config(noreplace) /etc/xinetd.d/rsync
%{_bindir}/rsync
%{_bindir}/rsync-ssl
