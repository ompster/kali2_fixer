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

print ' '
print ' '
print '============================================='
print 'upgrade and repair complete!'
print '============================================='
print ''

start_it = raw_input('Would you like to start Armitage now? (Y/N)')
start_it = start_it.upper()

if start_it == 'Y' :
	print 'starting armitage....'
	subprocess.call('armitage')

else :
	print 'Exiting script, thanks for using! - @ompster'



