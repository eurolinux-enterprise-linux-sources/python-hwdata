%if ! (0%{?fedora} || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:		python-hwdata
Version:	1.7.3
Release:	1%{?dist}
Summary:	Python bindings to hwdata package
BuildArch:  noarch
Group:		Development/Libraries
License:	GPLv2
URL:		https://fedorahosted.org/spacewalk/wiki/Projects/python-hwdata
Source0:	https://fedorahosted.org/releases/s/p/spacewalk/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: python-devel
Requires:	hwdata

%description
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

%prep
%setup -q


%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE example.py
%doc html
%{python_sitelib}/*


%changelog
* Fri Mar 02 2012 Miroslav Suchý 1.7.3-1
- 798375 - fix PCI device name translation (Joshua.Roys@gtri.gatech.edu)
- use setup from distutils

* Fri Mar 02 2012 Jan Pazdziora 1.7.2-1
- Update the copyright year info.

* Fri Mar 02 2012 Jan Pazdziora 1.7.1-1
- correct indentation (mzazrivec@redhat.com)

* Mon Oct 31 2011 Miroslav Suchý 1.6.2-1
- point URL to specific python-hwdata page

* Fri Jul 22 2011 Jan Pazdziora 1.6.1-1
- We only support version 14 and newer of Fedora, removing conditions for old
  versions.

* Mon Apr 26 2010 Miroslav Suchý <msuchy@redhat.com> 1.2-1
- 585138 - change %%files section and patial support for python3

* Fri Apr 23 2010 Miroslav Suchý <msuchy@redhat.com> 1.1-1
- initial release
