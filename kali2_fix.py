######################################
## Kali Linux 2 Fixer 				##
## By Nathan ASH 					##
## http://nathanash.id.au 			##
## @ompster - github.com/ompster 	##
######################################

import subprocess
import os



def fix_armitage_func():
	####FIX ARMITAGE####
	print 'We are about to download the the armitage fix for Kali 2, you need internet access!'
	raw_input('Press Enter to continue...')
	subprocess.call(['wget', 'http://www.fastandeasyhacking.com/download/armitage150813.tgz'])

	print 'Extracting downloaded archine into /usr/share/armitage'
	subprocess.call(['tar', 'xf', 'armitage150813.tgz', '-C', '/usr/share/armitage/', '--strip-components', '1'])

	print 'Starting PostgreSQL service...'
	subprocess.call(['service', 'postgresql', 'start'])

	print 'Initial msfDB schema creation....'
	subprocess.call(['msfdb', 'init'])


	start_it = raw_input('Would you like to start Armitage now? (Y/N)')
	start_it = start_it.upper()

	if start_it == 'Y' :
		print 'starting armitage....'
		subprocess.call('armitage')

	else :
		print 'Exiting script, thanks for using! - @ompster'
	####END FIX ARMITAGE####

def install_chrome_func() :
	print 'Installing Chromium, will first update sources...'
	os.system ('apt-get update')
	os.system ('apt-get chromium')
	exit()

print '''
KALI FIXER 2                                               
	'''
print '''
		What would you like to do?
		1. Fix armitage
		2. Install Chrome
		3. Exit
		'''
menu_option = raw_input('-> ')

if menu_option == "1" :
	fix_armitage_func()
elif menu_option == "2"
	install_chrome_func()
else :
	print '''
	http://github.com/ompster
	@ompster                      
	'''

	exit()




