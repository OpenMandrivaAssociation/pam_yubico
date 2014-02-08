%define _disable_ld_no_undefined 1

Summary:	Provides support for One Time Passwords (OTP) authentication
Name:		pam_yubico
Version:	2.4
Release:	5
License:	GPLv2
Group:		System/Libraries
URL:		http://code.google.com/p/yubico-pam/
Source0:	http://yubico-pam.googlecode.com/files/%{name}-%{version}.tar.gz
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README
%attr(0755,root,root) /%{_lib}/security/pam_yubico.so


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4-3mdv2011.0
+ Revision: 666982
- mass rebuild

* Wed Oct 20 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4-2mdv2011.0
+ Revision: 586955
- stupid build system
- fix build
- 2.4
- rebuilt for 2010.1
- rebuild

* Thu Jun 11 2009 Oden Eriksson <oeriksson@mandriva.com> 2.1-1mdv2010.0
+ Revision: 385140
- 2.1
- fix deps
- sync with fedora

* Wed Sep 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8-1mdv2009.0
+ Revision: 285433
- fix deps
- import pam_yubico


* Wed Sep 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8-1mdv2009.0
- initial Mandriva package
