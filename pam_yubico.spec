Summary:	Provides support for One Time Passwords (OTP) authentication
Name:		pam_yubico
Version:	2.1
Release:	%mkrel 1
License:	GPLv2
Group:		System/Libraries
URL:		http://code.google.com/p/yubico-pam/
Source0:	http://yubico-pam.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         64bit_pam.patch
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  ykclient-devel >= 2.3
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Yubico authentication device Yubikey generates one-time passwords that can
be used for authentication. This module allows you to use the Yubikey device to
authenticate to the PAM system.

The Yubico PAM module provides an easy way to integrate the Yubikey into your
existing user authentication infrastructure.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%serverbuild

%configure2_5x \
    --with-pam-dir=/%{_lib}/security

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}/%{_lib}/security/*.*a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README
%attr(0755,root,root) /%{_lib}/security/pam_yubico.so
