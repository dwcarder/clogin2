Name: 		clogin2         
Version: 	1.1
Release:        1
Summary: 	multi-vendor login tool, forked from RANCID

Group:          Applications/Internet
License:        BSD
URL:            https://github.com/dwcarder/clogin2
Source0:        %{name}-%{version}.tar.gz
BuildArch: 	noarch

Requires:       expect openssh tcl-syslog
Conflicts:	rancid

%description
%{summary}

%prep
%setup -q

%build
# Empty section

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/ns/bin
mkdir -p %{buildroot}/usr/local/ns/share/clogin2/doc
cp clogin2 %{buildroot}/usr/local/ns/bin
cp cloginrc %{buildroot}/usr/local/ns/share/clogin2/doc
cp LICENSE %{buildroot}/usr/local/ns/share/clogin2/doc

%clean
rm -rf %{buildroot}

%post
ln -s /usr/local/ns/bin/clogin2 /usr/local/ns/bin/clogin

%files
%defattr(755,root,root,-)
/usr/local/ns/bin/clogin2
%defattr(644,root,root,-)
/usr/local/ns/share/clogin2/doc/cloginrc
/usr/local/ns/share/clogin2/doc/LICENSE


%changelog
*Wed Jul 3 2014 <dwcarder@wisc.edu> 1.0-1 --Initial Packaging Build.
*Wed Jul 9 2014 <dwcarder@wisc.edu> 1.1-1 --Fixes to tcl-syslog
