FreeBSD Send-PR Tool
====================

Requirements
------------

Install these::

    # cd /usr/ports/ports-mgmt/genplist; make install clean
    # cd /usr/ports/ports-mgmt/porttools; make install clean
    # cd /usr/ports/devel/py-lxml; make install clean

Create your ~/.porttools::

    # FreeBSD Port Tools configuration file – see porttools(5)
    # vim: ft=sh
    EMAIL="your@email.address"
    FULLNAME="Your Name"
    ORGANIZATION="FreeBSD @ Taiwan"
    BUILDROOT="/tmp"
    ARCHIVE_DIR=""
    DIFF_MODE=".orig" 
    DIFF_VIEWER="more"
    PORTLINT_FLAGS="abct"


Then, check http://portscout.org/rss/rss.cgi?r=recent for any ports updates

Usage
-----

Choose what update do you want to send-pr, for example::

    devel/py-parsing: 1.5.5 -> 1.5.6
    Update found for port devel/py-parsing: version 1.5.5 to 1.5.6

Then, you can use this script to help you copy /usr/ports/devel/py-parsing to 
/usr/ports/devel/py-parsing.orig, generate the pkg-plist, and take you to the ports directory::

    # . up devel/py-parsing: version 1.5.5 to 1.5.6

If there is other same port pr be found, it will provide you the pr link to check it.

Type less words?
----------------

Yes, you can::

    # . up2 devel/py-parsing 1.5.5 1.5.6

or use up.py (but will not take you to the ports directory)::

    # ./up.py devel/py-parsing 1.5.5 1.5.6

