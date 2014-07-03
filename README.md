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

## Instalation
There are a few options: use as-is standalone, or you can optionally edit the included spec file and build an RPM to your liking.  You must also point the script the cloginrc file.  For example, a user may copy this to ~/.cloginrc and customize it as needed.

## Contributers to clogin2 include:
* Henry Kilmer, Erik Sherk and Pete Whiting, for the original clogin
* Dave Plonka
* Elle Janet Plato
* Dale W. carder
