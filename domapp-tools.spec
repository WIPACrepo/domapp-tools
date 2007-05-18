Summary: IceCube DOM Application (domapp) testing applications
Name: domapp-tools
Version: %{VER}
Release: %{REL}
URL: http://docushare.icecube.wisc.edu/docushare/dsweb/View/Collection-1416
Source0: %{name}-%{version}.tgz
License: Copyright 2003 IceCube collaboration
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-root
Prefix: %{_prefix}
Requires: perl > 5.0
Requires: domhub-tools >= 100
Requires: moat >= 0.0.4
Requires: python >= 2.2

%description
IceCube DOM Application (domapp) testing applications

%prep

%setup -q

%build
make clean; make

%install
install -d ${RPM_BUILD_ROOT}/usr/local/share
install -d ${RPM_BUILD_ROOT}/usr/local/bin

install domapp-tools-version ${RPM_BUILD_ROOT}/usr/local/share
install domapptest           ${RPM_BUILD_ROOT}/usr/local/bin
install upload_domapp.pl     ${RPM_BUILD_ROOT}/usr/local/bin
install uda.pl               ${RPM_BUILD_ROOT}/usr/local/bin
install decomp               ${RPM_BUILD_ROOT}/usr/local/bin
install decodemoni           ${RPM_BUILD_ROOT}/usr/local/bin
install decodeeng            ${RPM_BUILD_ROOT}/usr/local/bin
install decodesn             ${RPM_BUILD_ROOT}/usr/local/bin
install domapp_multitest.pl  ${RPM_BUILD_ROOT}/usr/local/bin
install domapp-versions      ${RPM_BUILD_ROOT}/usr/local/bin
install domapp.py            ${RPM_BUILD_ROOT}/usr/local/bin
install domapptest.py        ${RPM_BUILD_ROOT}/usr/local/bin
install dor.py               ${RPM_BUILD_ROOT}/usr/local/bin
install exc_string.py        ${RPM_BUILD_ROOT}/usr/local/bin
install minitimer.py         ${RPM_BUILD_ROOT}/usr/local/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/share/domapp-tools-version
/usr/local/bin/domapptest
/usr/local/bin/upload_domapp.pl
/usr/local/bin/uda.pl
/usr/local/bin/decomp
/usr/local/bin/decodemoni
/usr/local/bin/decodeeng
/usr/local/bin/decodesn
/usr/local/bin/domapp_multitest.pl
/usr/local/bin/domapp-versions
/usr/local/bin/domapp.py
/usr/local/bin/domapptest.py
/usr/local/bin/dor.py
/usr/local/bin/exc_string.py
/usr/local/bin/minitimer.py

%post
ln -f -s /usr/local/bin/domapp_multitest.pl /usr/local/bin/dmt

%postun
rm -f /usr/local/bin/dmt

%changelog
* Fri May 18 2007 John E. Jacobsen <john@mail.npxdesigns.com>
- Add python tests
* Tue Jul 13 2005 John E. Jacobsen <jacobsen@npxdesigns.com>
- Changes to fit into domapp project
* Mon Jun 20 2005 Martin C. Stoufer <MCStoufer@lbl.gov>
- Initial build.


