Name:		fixup-container-notices 
Version:	1
Release:	1
Summary:	Fixup missing container notices
Group:		System Environment/Base
License:	MIT
URL:		http://github.com/atgreen/fixup-container-notices
Source0:	fixup-container-notices.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
An imperfect but useful script to replace missing notices within a
container image.

%prep
%setup -q -n fixup-container-notices

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/fixup-container-notices
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp -a notices/* $RPM_BUILD_ROOT/usr/share/fixup-container-notices
cp -a fixup-container-notices $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root, 0755)
/usr/share/fixup-container-notices
%{_bindir}/fixup-container-notices

%changelog
* Fri Feb 15 2019 Anthony Green <green@redhat.com> - 1-1
- Created
