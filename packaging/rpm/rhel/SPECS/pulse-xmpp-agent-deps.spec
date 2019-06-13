%global __provides_exclude_from ^%_var/lib/tomcat/webapps/guacamole/classpath/.*$

%define use_git                1
%define git                    SHA

Summary:	Dependancies needed for pulse windows agent
Name:		pulse-xmpp-agent-deps
Version:	1.7
%if ! %use_git
Release:        0%{?dist}
%else
Release:        0.%git.1%{?dist}
%endif
Source0:	%{name}-%{version}.tar.gz
Source1:     https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi
Source2:     https://www.python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi
Source3:     https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe
Source4:     https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe
Source5:     https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi
Source6:     https://agents.siveo.net/win/downloads/libcurl4-7.52.1-1.tar.xz
Source7:     https://agents.siveo.net/win/downloads/cwRsync_5.5.0_x86_Free.zip
Source8:     https://github.com/PowerShell/Win32-OpenSSH/releases/download/v0.0.21.0/OpenSSH-Win32.zip
Source9:     https://github.com/PowerShell/Win32-OpenSSH/releases/download/v0.0.21.0/OpenSSH-Win64.zip
Source10:    https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.4.2/fusioninventory-agent_windows-x86_2.4.2.exe
Source11:    https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.4.2/fusioninventory-agent_windows-x86_2.4.2-portable.exe
Source12:    https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.4.2/fusioninventory-agent_windows-x64_2.4.2.exe
Source13:    https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.4.2/fusioninventory-agent_windows-x64_2.4.2-portable.exe
Source14:    https://github.com/stascorp/rdpwrap/releases/download/v1.6.1/RDPWrap-v1.6.1.zip
Source15:    https://www.tightvnc.com/download/2.8.8/tightvnc-2.8.8-gpl-setup-32bit.msi
Source16:    https://www.tightvnc.com/download/2.8.8/tightvnc-2.8.8-gpl-setup-64bit.msi
Source17:    https://github.com/stweil/OSXvnc/releases/download/V5_2_1/OSXvnc-5.2.1.dmg
Source18:    https://github.com/Homebrew/brew/archive/1.5.12.tar.gz
Source19:    https://github.com/syncthing/syncthing/releases/download/v1.1.0/syncthing-windows-386-v1.1.0.zip
Source20:    https://github.com/syncthing/syncthing/releases/download/v1.1.0/syncthing-windows-amd64-v1.1.0.zip
Source21:    https://github.com/syncthing/syncthing/releases/download/v1.1.0/syncthing-macos-amd64-v1.1.0.tar.gz
Source22:    https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.4/FusionInventory-Agent-2.4-1.pkg.tar.gz

Source100:   https://pypi.python.org/packages/cd/59/7cc2407b15bcd13d43933a5ae163de89b6f366dda8b2b7403453e61c3a05/pypiwin32-219-cp27-none-win32.whl
Source101:   https://files.pythonhosted.org/packages/a5/8d/739f12d811d19cd6686f97bb96b65b0e4c8ca428fb02581d872b912b14cf/pypiwin32-219-cp27-none-win_amd64.whl
Source102:   https://pypi.python.org/packages/a7/4c/8e0771a59fd6e55aac993a7cc1b6a0db993f299514c464ae6a1ecf83b31d/netifaces-0.10.5.tar.gz
Source103:   https://pypi.python.org/packages/85/11/722b9ce6725bf8160bd8aca68b1e61bd9db422ab12dae28daa7defab2cdc/comtypes-1.1.3-2.zip
Source104:   https://pypi.python.org/packages/7c/69/c2ce7e91c89dc073eb1aa74c0621c3eefbffe8216b3f9af9d3885265c01c/configparser-3.5.0.tar.gz
Source105:   https://pypi.python.org/packages/07/49/42c86388fed58455e7e18d3821d7687f4921e47a40cb312e69b82f75c660/utils-0.9.0.tar.gz
Source106:   https://pypi.python.org/packages/2e/33/7adcc8d6b35cb72f9cc56785a3d9c63d540200c476b0cb3a0926f5b51102/sleekxmpp-1.3.1.tar.gz
Source107:   https://pypi.python.org/packages/03/2d/cbf13257c0115bef37b6b743758411cec70c565405cbd08d0f7059bc715f/WMI-1.4.9.zip
Source108:   https://pypi.python.org/packages/60/ad/d6bc08f235b66c11bbb76df41b973ce93544a907cc0e23c726ea374eee79/zipfile2-0.0.12-py2.py3-none-any.whl
Source109:   https://files.pythonhosted.org/packages/69/f1/387306c495d8f9b6518ea35348668bc1e8bf56b9c7f1425b5f12df79c356/pycurl-7.43.0-cp27-none-win32.whl
Source110:   https://files.pythonhosted.org/packages/a6/5f/09e4740d4ec0c273e2a6ebbceb3d90f4be52f46d94ccac2639c9328e397b/pycurl-7.43.0-cp27-none-win_amd64.whl
Source111:   https://pypi.python.org/packages/f1/c7/e19d317cc948095abc872a6e6ae78ac80260f2b45771dfa7a7ce86865f5b/lxml-3.6.0-cp27-none-win32.whl
Source112:   https://files.pythonhosted.org/packages/35/a7/6a1a44d3a37358f8fda5d1b992c837cb2db8940293c2d84faa145f29e88a/lxml-3.6.0-cp27-none-win_amd64.whl
Source113:   https://pypi.python.org/packages/60/db/645aa9af249f059cc3a368b118de33889219e0362141e75d4eaf6f80f163/pycrypto-2.6.1.tar.gz
Source114:   https://pypi.python.org/packages/58/2a/17d003f2a9a0188cf9365d63b3351c6522b7d83996b70270c65c789e35b9/croniter-0.3.16.tar.gz
Source115:   https://pypi.python.org/packages/40/8b/275015d7a9ec293cf1bbf55433258fbc9d0711890a7f6dc538bac7b86bce/python_dateutil-2.6.0-py2.py3-none-any.whl
Source116:   https://pypi.python.org/packages/c8/0a/b6723e1bc4c516cb687841499455a8505b44607ab535be01091c0f24f079/six-1.10.0-py2.py3-none-any.whl
Source117:   https://pypi.python.org/packages/e5/cc/6dd427e738a8db6d0b66525856da43d2ef12c4c19269863927f7cf0e2aaf/psutil-5.4.3-cp27-none-win32.whl
Source118:   https://files.pythonhosted.org/packages/b9/e4/6867765edcab8d12a52c84c9b0af492ecb99f8cc565ad552341bcf73ebd9/psutil-5.4.3-cp27-none-win_amd64.whl
Source119:   https://github.com/mhammond/pywin32/releases/download/b223/pywin32-223.win32-py3.6.exe
Source120:   https://github.com/mhammond/pywin32/releases/download/b223/pywin32-223.win-amd64-py3.6.exe
Source121:   https://files.pythonhosted.org/packages/6c/63/89f888968ee0c7e7ffb2ea7604fae3ef85f7bc86f57dd07019805aa78798/PyQt5-5.10.1-5.10.1-cp35.cp36.cp37.cp38-none-win32.whl
Source122:   https://files.pythonhosted.org/packages/a7/22/67cc2bac6ae2cd3a7eabb2a2e91638b94bdc6e0503747e49670ce44bb5b0/PyQt5-5.10.1-5.10.1-cp35.cp36.cp37.cp38-none-win_amd64.whl
Source123:   https://files.pythonhosted.org/packages/7a/49/67cc7955baf2ec5b67e141da2ab2a436cbf0f8d7c9fcab54e35df21d056b/sip-4.19.8-cp36-none-win32.whl
Source124:   https://files.pythonhosted.org/packages/30/fa/90ea79d7b6b21a50e16d2e1214bd4d45390ee1b5393dc09c3785a3dc9c7e/sip-4.19.8-cp36-none-win_amd64.whl
Source125:   https://files.pythonhosted.org/packages/a2/38/3adebc116c711f795edb94004afbd9784576b6ee50b7f89647889382d152/tray-0.1.0.tar.gz
Source126:   https://pypi.python.org/packages/77/d9/d272b38e6e25d2686e22f6058820298dadead69340b1c57ff84c87ef81f0/pycurl-7.43.0.1.tar.gz
Source127:   https://pypi.python.org/packages/11/1b/fe6904151b37a0d6da6e60c13583945f8ce3eae8ebd0ec763ce546358947/lxml-3.6.0.tar.gz
Source128:   https://pypi.python.org/packages/e2/e1/600326635f97fee89bf8426fef14c5c29f4849c79f68fd79f433d8c1bd96/psutil-5.4.3.tar.gz
Source129:   https://pypi.python.org/packages/28/df/755dab9f83c37031aea1cd9915673b5633665c575d649e812657df95b944/plyvel-1.0.1.tar.gz
Source130:   https://files.pythonhosted.org/packages/36/60/45f30390a38b1f92e0a8cf4de178cd7c2bc3f874c85430e40ccf99df8fe7/pysftp-0.2.9.tar.gz
Source131:   https://files.pythonhosted.org/packages/ef/4e/9f04fc58040cbf05984d7ca9393ff2dbc8b6909b163a768fc28786eacf06/syncthing-2.3.1.tar.gz
Source132:   https://files.pythonhosted.org/packages/7d/e3/20f3d364d6c8e5d2353c72a67778eb189176f08e873c9900e10c0287b84b/requests-2.21.0-py2.py3-none-any.whl

License:	MIT
Group:		Development/Java
Url:		http://www.siveo.org/
BuildArch:	noarch

%description
Dependancies needed for pulse windows agent


%package -n pulse-kiosk-agent-deps
Summary:    Dependancies needed for kiosk windows agent
Group:      System/Servers
Requires:   pulse2-common = %version-%release

%description -n pulse-kiosk-agent-deps
Dependancies needed for kiosk windows agent

%prep
%setup -q -c

%build

%install
mkdir -p %buildroot/var/lib/pulse2/clients/win/downloads/
cp %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9 %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 %SOURCE15 %SOURCE16 %SOURCE19 %SOURCE20 %buildroot/var/lib/pulse2/clients/win/downloads/
mkdir -p %buildroot/var/lib/pulse2/clients/win/downloads/python_modules/
cp %SOURCE100 %SOURCE101 %SOURCE102 %SOURCE103 %SOURCE104 %SOURCE105 %SOURCE106 %SOURCE107 %SOURCE108 %SOURCE109 %SOURCE110 %SOURCE111 %SOURCE112 %SOURCE113 %SOURCE114 %SOURCE115 %SOURCE116 %SOURCE117 %SOURCE118 %SOURCE119 %SOURCE120 %SOURCE121 %SOURCE122 %SOURCE123 %SOURCE124 %SOURCE125 %SOURCE126 %SOURCE130 %SOURCE131 %SOURCE132 %buildroot/var/lib/pulse2/clients/win/downloads/python_modules/

mkdir -p %buildroot/var/lib/pulse2/clients/linux/downloads/python_modules/

mkdir -p %buildroot/var/lib/pulse2/clients/mac/downloads/
cp %SOURCE17 %SOURCE18 %SOURCE21 %SOURCE22 %buildroot/var/lib/pulse2/clients/mac/downloads/
mkdir -p %buildroot/var/lib/pulse2/clients/mac/downloads/python_modules/
cp %SOURCE102 %SOURCE104 %SOURCE105 %SOURCE106 %SOURCE108 %SOURCE113 %SOURCE114 %SOURCE115 %SOURCE116 %SOURCE126 %SOURCE127 %SOURCE128 %SOURCE129 %SOURCE130 %SOURCE131 %SOURCE132  %buildroot/var/lib/pulse2/clients/mac/downloads/python_modules/


%files
/var/lib/pulse2/clients/linux/downloads/
/var/lib/pulse2/clients/mac/downloads/
/var/lib/pulse2/clients/win/downloads/
%exclude /var/lib/pulse2/clients/win/downloads/python-3.6.5.exe
%exclude /var/lib/pulse2/clients/win/downloads/python-3.6.5-amd64.exe
%exclude /var/lib/pulse2/clients/win/downloads/python_modules/pywin32-223.win32-py3.6.exe
%exclude /var/lib/pulse2/clients/win/downloads/python_modules/pywin32-223.win-amd64-py3.6.exe
%exclude /var/lib/pulse2/clients/win/downloads/python_modules/PyQt5-5.10.1-5.10.1-cp35.cp36.cp37.cp38-none-win32.whl
%exclude /var/lib/pulse2/clients/win/downloads/python_modules/PyQt5-5.10.1-5.10.1-cp35.cp36.cp37.cp38-none-win_amd64.whl
%exclude /var/lib/pulse2/clients/win/downloads/python_modules/sip-4.19.8-cp36-none-win32.whl
%exclude /var/lib/pulse2/clients/win/downloads/python_modules/sip-4.19.8-cp36-none-win_amd64.whl
%exclude /var/lib/pulse2/clients/win/downloads/python_modules/tray-0.1.0.tar.gz

%files -n pulse-kiosk-agent-deps
/var/lib/pulse2/clients/win/downloads/python-3.6.5.exe
/var/lib/pulse2/clients/win/downloads/python-3.6.5-amd64.exe
/var/lib/pulse2/clients/win/downloads/python_modules/pywin32-223.win32-py3.6.exe
/var/lib/pulse2/clients/win/downloads/python_modules/pywin32-223.win-amd64-py3.6.exe
/var/lib/pulse2/clients/win/downloads/python_modules/PyQt5-5.10.1-5.10.1-cp35.cp36.cp37.cp38-none-win32.whl
/var/lib/pulse2/clients/win/downloads/python_modules/PyQt5-5.10.1-5.10.1-cp35.cp36.cp37.cp38-none-win_amd64.whl
/var/lib/pulse2/clients/win/downloads/python_modules/sip-4.19.8-cp36-none-win32.whl
/var/lib/pulse2/clients/win/downloads/python_modules/sip-4.19.8-cp36-none-win_amd64.whl
/var/lib/pulse2/clients/win/downloads/python_modules/tray-0.1.0.tar.gz
