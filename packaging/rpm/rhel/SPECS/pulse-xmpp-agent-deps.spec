%global __provides_exclude_from ^%_var/lib/tomcat/webapps/guacamole/classpath/.*$

%define use_git                1
%define git                    SHA

Summary:	Dependancies needed for pulse windows agent
Name:		pulse-xmpp-agent-deps
Version:	1.6
%if ! %use_git
Release:        0%{?dist}
%else
Release:        0.%git.1%{?dist}
%endif
Source0:	%{name}-%{version}.tar.gz
Source1:    https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi
Source17:   https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi
Source2:    https://agents.siveo.net/win/libcurl4-7.52.1-1.tar.xz
Source3:	https://agents.siveo.net/win/cwRsync_5.5.0_x86_Free.zip
Source4:	https://github.com/PowerShell/Win32-OpenSSH/releases/download/v0.0.21.0/OpenSSH-Win32.zip
Source5:	https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.4/fusioninventory-agent_windows-x86_2.4.exe
Source6:	https://pypi.python.org/packages/cd/59/7cc2407b15bcd13d43933a5ae163de89b6f366dda8b2b7403453e61c3a05/pypiwin32-219-cp27-none-win32.whl
Source7:	https://pypi.python.org/packages/a7/4c/8e0771a59fd6e55aac993a7cc1b6a0db993f299514c464ae6a1ecf83b31d/netifaces-0.10.5.tar.gz
Source8:	https://pypi.python.org/packages/85/11/722b9ce6725bf8160bd8aca68b1e61bd9db422ab12dae28daa7defab2cdc/comtypes-1.1.3-2.zip
Source9:	https://pypi.python.org/packages/7c/69/c2ce7e91c89dc073eb1aa74c0621c3eefbffe8216b3f9af9d3885265c01c/configparser-3.5.0.tar.gz
Source10:	https://pypi.python.org/packages/07/49/42c86388fed58455e7e18d3821d7687f4921e47a40cb312e69b82f75c660/utils-0.9.0.tar.gz
Source11:	https://pypi.python.org/packages/2e/33/7adcc8d6b35cb72f9cc56785a3d9c63d540200c476b0cb3a0926f5b51102/sleekxmpp-1.3.1.tar.gz
Source12:	https://pypi.python.org/packages/03/2d/cbf13257c0115bef37b6b743758411cec70c565405cbd08d0f7059bc715f/WMI-1.4.9.zip
Source13:	https://pypi.python.org/packages/60/ad/d6bc08f235b66c11bbb76df41b973ce93544a907cc0e23c726ea374eee79/zipfile2-0.0.12-py2.py3-none-any.whl
Source14:	https://files.pythonhosted.org/packages/69/f1/387306c495d8f9b6518ea35348668bc1e8bf56b9c7f1425b5f12df79c356/pycurl-7.43.0-cp27-none-win32.whl
Source15:	https://pypi.python.org/packages/f1/c7/e19d317cc948095abc872a6e6ae78ac80260f2b45771dfa7a7ce86865f5b/lxml-3.6.0-cp27-none-win32.whl
Source16:	https://pypi.python.org/packages/60/db/645aa9af249f059cc3a368b118de33889219e0362141e75d4eaf6f80f163/pycrypto-2.6.1.tar.gz
Source18:   https://pypi.python.org/packages/58/2a/17d003f2a9a0188cf9365d63b3351c6522b7d83996b70270c65c789e35b9/croniter-0.3.16.tar.gz
Source19:   https://pypi.python.org/packages/40/8b/275015d7a9ec293cf1bbf55433258fbc9d0711890a7f6dc538bac7b86bce/python_dateutil-2.6.0-py2.py3-none-any.whl
Source20:   https://pypi.python.org/packages/c8/0a/b6723e1bc4c516cb687841499455a8505b44607ab535be01091c0f24f079/six-1.10.0-py2.py3-none-any.whl
Source21:   https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.4/fusioninventory-agent_windows-x86_2.4-portable.exe
Source22:   https://github.com/PowerShell/Win32-OpenSSH/releases/download/v0.0.21.0/OpenSSH-Win64.zip
Source23:   https://github.com/stascorp/rdpwrap/releases/download/v1.6.1/RDPWrap-v1.6.1.zip
Source24:   https://www.tightvnc.com/download/2.8.8/tightvnc-2.8.8-gpl-setup-32bit.msi
Source27:   https://pypi.python.org/packages/5b/68/436ce631dc0584969d03186d095f4daf09b5c0193ebd66927524a33411c8/pypiwin32-219-cp35-none-win32.whl
Source28:   https://pypi.python.org/packages/e5/cc/6dd427e738a8db6d0b66525856da43d2ef12c4c19269863927f7cf0e2aaf/psutil-5.4.3-cp27-none-win32.whl
Source29:   https://github.com/stweil/OSXvnc/releases/download/V5_2_1/OSXvnc-5.2.1.dmg
Source34:   https://github.com/Homebrew/brew/archive/1.5.12.tar.gz
Source35:   https://pypi.python.org/packages/77/d9/d272b38e6e25d2686e22f6058820298dadead69340b1c57ff84c87ef81f0/pycurl-7.43.0.1.tar.gz
Source36:   https://www.python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi
Source37:   https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.4/fusioninventory-agent_windows-x64_2.4.exe
Source38:   https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.4/fusioninventory-agent_windows-x64_2.4-portable.exe
Source39:   https://www.tightvnc.com/download/2.8.8/tightvnc-2.8.8-gpl-setup-64bit.msi
Source40:   https://files.pythonhosted.org/packages/a6/5f/09e4740d4ec0c273e2a6ebbceb3d90f4be52f46d94ccac2639c9328e397b/pycurl-7.43.0-cp27-none-win_amd64.whl
Source41:   https://files.pythonhosted.org/packages/35/a7/6a1a44d3a37358f8fda5d1b992c837cb2db8940293c2d84faa145f29e88a/lxml-3.6.0-cp27-none-win_amd64.whl
Source42:   https://files.pythonhosted.org/packages/b9/e4/6867765edcab8d12a52c84c9b0af492ecb99f8cc565ad552341bcf73ebd9/psutil-5.4.3-cp27-none-win_amd64.whl
Source43:   https://files.pythonhosted.org/packages/a5/8d/739f12d811d19cd6686f97bb96b65b0e4c8ca428fb02581d872b912b14cf/pypiwin32-219-cp27-none-win_amd64.whl
License:	MIT
Group:		Development/Java
Url:		http://www.siveo.org/
BuildArch:	noarch

%description
Dependancies needed for pulse windows agent

%prep
%setup -q -c

%build

%install
mkdir -p %buildroot/var/lib/pulse2/clients/win32/downloads/
cp %SOURCE1 %SOURCE36 %SOURCE17 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE37 %SOURCE21 %SOURCE38 %SOURCE22 %SOURCE23 %SOURCE24 %SOURCE39 %buildroot/var/lib/pulse2/clients/win32/downloads/
mkdir -p %buildroot/var/lib/pulse2/clients/win32/downloads/python_modules/
cp %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9 %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 %SOURCE40 %SOURCE15 %SOURCE41 %SOURCE16 %SOURCE18 %SOURCE19 %SOURCE20 %SOURCE27 %SOURCE28 %SOURCE42 %SOURCE43 %buildroot/var/lib/pulse2/clients/win32/downloads/python_modules/

mkdir -p %buildroot/var/lib/pulse2/clients/linux/downloads/python_modules/

mkdir -p %buildroot/var/lib/pulse2/clients/mac/downloads/
cp %SOURCE29 %SOURCE34 %buildroot/var/lib/pulse2/clients/mac/downloads/
mkdir -p %buildroot/var/lib/pulse2/clients/mac/downloads/python_modules/
cp %SOURCE7 %SOURCE9 %SOURCE10 %SOURCE11 %SOURCE13 %SOURCE14 %SOURCE15 %SOURCE16 %SOURCE18  %SOURCE19 %SOURCE20 %SOURCE35 %buildroot/var/lib/pulse2/clients/mac/downloads/python_modules/

%files
/var/lib/pulse2/clients/linux/downloads/
/var/lib/pulse2/clients/mac/downloads/
/var/lib/pulse2/clients/win32/downloads/
