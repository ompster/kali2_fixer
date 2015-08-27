######################################
## Kali Linux 2 Fixer 				##
## By Nathan ASH 					##
## http://nathanash.id.au 			##
## @ompster - github.com/ompster 	##
######################################

import subprocess

print 'We are about to download the the armitage fix for Kali 2, you need internet access!'
raw_input('Press Enter to continue...')
subprocess.call(['wget', 'http://www.fastandeasyhacking.com/download/armitage150813.tgz'])

print 'Extracting downloaded archine into /usr/share/armitage'
subprocess.call(['tar', 'xf', 'armitage150813.tgz', '-C', '/usr/share/armitage/', '--strip-components', '1'])

print 'Starting PostgreSQL service...'
subprocess.call(['service', 'postgresql', 'start'])

print 'Initial msfDB schema creation....'
subprocess.call(['msfdb', 'init'])

