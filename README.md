# clogin2

clogin2 is a fork of the clogin tool that ships with [RANCID](http://www.shrubbery.net/rancid/).

We forked RANCID internally around the year 2001, and hacked it up to do various things like support various vendors, answer yes/no prompts, use ssh, handle tftp output, syslog when it is invoked, and probably more.  

This is used as the primary login tool used for almost all automated configuration of network devices at UW.  At this point, some amount of that logic is based on the DNS naming convention used, but that could probably be fixed easily with by hacking the script, or with the addition of a config file.

## Things we know that work with clogin2:
* Juniper JunOS
* Cisco IOS-XR
* Cisco NX-OS
* Cisco IOS-XE
* Cisco IOS (classic)
* Cisco ASA firewalls
* Cisco FWSM firewalls
* Alteon loadbalancers

## Installation
There are a few options: 
* Use as-is standalone.
* Edit the included spec file, build and install an RPM to your liking:
```bash
git clone http://github.com/dwcarder/clogin2.git
mv clogin2 clogin2-1.0
tar -cf clogin2-1.0.tar clogin2-1.0
gzip clogin2-1.0.tar
cp clogin2-1.0.tar.gz ~/rpmbuild/SOURCES
cp clogin2-1.0/clogin2.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS
rpmbuild -bb clogin2.spec
rpm -Uvh ~/rpmbuild/RPMS/noarch/clogin2-1.0-1.noarch.rpm
```

## Usage:
```bash
Usage: clogin2 [-autoenable] [-noenable] [-c command]  [-Evar=x] [-e enable-password] [-f cloginrc-file] [-p user-password]  [-s script-file] [-t timeout] [-u username]  [-v vty-password] [-w enable-username] [-x command-file]  [-y ssh_cypher_type] router [router...]
```

You must point the script to a cloginrc file.  Optionally, a user may copy this to ~/.cloginrc and customize it as needed.


## Contributers to clogin2 include:
* Henry Kilmer, Erik Sherk and Pete Whiting, for the original clogin
* Dave Plonka
* Elle Janet Plato
* Michael Hare
* Dale W. carder

## LICENSE
The clogin2 script at this time maintains the original license, which is restricted to non-commercial usage.  Other items in this distribution, including the rpm spec file and this README are licensed with the BSD 2-Clause License and Copyright (C) 2014 The University of Wisconsin Board of Regents.  See the LICENSE file for details.


