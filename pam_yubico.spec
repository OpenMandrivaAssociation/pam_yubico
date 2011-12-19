Summary:	Provides support for One Time Passwords (OTP) authentication
Name:		pam_yubico
Version:	2.10
Release:	1
License:	GPLv2
Group:		System/Libraries
URL:		http://code.google.com/p/yubico-pam/
Source0:	http://yubico-pam.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	http://yubico-pam.googlecode.com/files/%{name}-%{version}.tar.gz.sig
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  ykclient-devel >= 2.3
BuildRequires:  libyubikey-devel
BuildRequires:  ykpers-devel

Patch0:		pam_yubico-2.10-config.patch

%description
The Yubico authentication device Yubikey generates one-time passwords that can
be used for authentication. This module allows you to use the Yubikey device to
authenticate to the PAM system.

The Yubico PAM module provides an easy way to integrate the Yubikey into your
existing user authentication infrastructure.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1
autoreconf -ifs

%build
%serverbuild

%configure2_5x \
    --libdir=/%{_lib} \
    --with-pam-dir=/%{_lib}/security

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}/%{_lib}/security/*.*a
rm -f %{buildroot}%{_includedir}/*.h

%files
%doc COPYING ChangeLog NEWS README doc
%attr(0755,root,root) /%{_lib}/security/pam_yubico.so
%attr(0755,root,root) %{_bindir}/ykpamcfg
%attr(0644,root,root) %{_mandir}/man1/ykpamcfg.1*
