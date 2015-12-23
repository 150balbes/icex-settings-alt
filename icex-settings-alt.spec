Name: icex-settings-alt
Version: 0.0.1
Release: alt2

License: GPL
Group: Graphical desktop/Icewm
URL: https://github.com/150balbes/icewm-settings-altlinux
Summary: A settings altlinux for IceWM
BuildArch: noarch

Requires: icewm-theme-AltClearlooks

Conflicts: design-icewm

Source0: icewm.tar

%description
A settings altlinux for IceWM

%prep
%build
%install
mkdir -p %buildroot%_sysconfdir/icewm
tar xf %SOURCE0 -C %buildroot%_sysconfdir/

%files
%_sysconfdir/icewm

%changelog
* Mon Dec 22 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt2
- edit reboot and shutdown command

* Mon Dec 14 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 0.0.1-alt1
- new version
