%define _disable_ld_no_undefined 1

Summary:	Provides support for One Time Passwords (OTP) authentication
Name:		pam_yubico
Version:	2.4
Release:	7
License:	GPLv2
Group:		System/Libraries
Url:		http://code.google.com/p/yubico-pam/
Source0:	http://yubico-pam.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	ykclient-devel >= 2.3

%description
The Yubico authentication device Yubikey generates one-time passwords that can
be used for authentication. This module allows you to use the Yubikey device to
authenticate to the PAM system.

The Yubico PAM module provides an easy way to integrate the Yubikey into your
existing user authentication infrastructure.

%prep
%setup -q

%build
%serverbuild
%configure2_5x \
	--disable-static \
	--libdir=/%{_lib} \
	--with-pam-dir=/%{_lib}/security

%make

%install
%makeinstall_std

%files
%doc COPYING ChangeLog NEWS README
/%{_lib}/security/pam_yubico.so

