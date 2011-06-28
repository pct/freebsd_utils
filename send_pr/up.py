#!/usr/bin/env python
# coding: utf-8

import sys
import os
from os import system
import lxml.html as lhtml

PR_CHECK_URL = 'http://www.freebsd.org/cgi/query-pr-summary.cgi?category=&severity=&priority=&class=&state=&sort=none&text=PORT_NAME&responsible=&multitext=&originator=&release='

def gen_port(port_dir, port_old_ver, port_new_ver):
    check_pr_ret = check_pr(port_dir, port_new_ver)
    if check_pr_ret:
        os.chdir('/usr/ports')
        if os.getcwd() == '/usr/ports':
            system('rm -rf ' + port_dir + '.orig; cp -rpf ' + port_dir + ' ' + port_dir + '.orig')
            os.chdir('/usr/ports/' + port_dir)
            if os.getcwd() == '/usr/ports/' + port_dir:
                # 檢查原先的 Makefile 是否 PORTVERSION 版本是所提供的舊版
                f = open('Makefile', 'r')
                r = f.read()
                f.close()
                if port_old_ver not in r:
                    print('Original version is not found in Makefile, exit!')
                    sys.exit(1)
                # 如果是，繼續執行
                system('sed -i .orig -e "s|' + port_old_ver + '|'+ port_new_ver +'|" Makefile')
                system('make makesum; genplist create /tmp; rm Makefile.orig')
                if not os.path.exists('pkg-plist'):
                    system('rm pkg-plist.new; genplist test; genplist clean')
        else:
            sys.exit(1)
    else:
        print('Please recheck: ' + PR_CHECK_URL.replace('PORT_NAME', port_dir.split('/')[1]))
        sys.exit(1)

def check_pr(port_dir, port_new_ver):
    url = PR_CHECK_URL.replace('PORT_NAME', port_dir.split('/')[1])

    try:
        ret = lhtml.parse(url).xpath('//h1')[1].text
    except IndexError:
        ret = 'False'

    return ret == 'No matches to your query'


if __name__ == '__main__':
    if 'version' in sys.argv and 'to' in sys.argv:
        sys.argv.remove('version')
        sys.argv.remove('to')
        sys.argv[1] = sys.argv[1].replace(':', '')
        gen_port(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        if len(sys.argv) < 3:
            print('Usage: up <port_cat/port_name> <orig_version> <new_version>')
        else:
            gen_port(sys.argv[1], sys.argv[2], sys.argv[3])
