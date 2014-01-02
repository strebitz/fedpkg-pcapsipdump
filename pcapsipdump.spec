Name:		pcapsipdump
Version:	0.2
Release:	1%{?dist}
Summary:	libpcap-based SIP sniffer with per-call sorting capabilities

Group:		System/Utilities
License:	GPLv2
URL:		http://pcapsipdump.sourceforge.net/
Source0:    http://downloads.sourceforge.net/project/pcapsipdump/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot:  /var/tmp/%{name}-%{version}

BuildRequires:	libpcap-devel
Requires:	libpcap

%description
pcapsipdump is libpcap-based SIP sniffer with per-call sorting capabilities.
It writes SIP/RTP sessions to disk in a same format, as "tcpdump -w",
but one file per SIP session (even if there is thousands of concurrent SIP sessions)

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/usr/sbin %{buildroot}/etc/sysconfig %{buildroot}/etc/rc.d/init.d %{buildroot}/var/spool
make install DESTDIR=%{buildroot}


%files
%doc
%config(noreplace) %attr(0755,root,root) /etc/sysconfig/pcapsipdump
%attr(0700,root,root) %dir    /var/spool/pcapsipdump
%attr(0755,root,root)       /etc/rc.d/init.d/pcapsipdump
%attr(0755,root,root)      /usr/sbin/pcapsipdump



%changelog
* Wed Jan 1 2014 Sebastian Trebitz <sebastian@trebitz.eu> 0.2-1
- Initial release of the package and spec file
