######################################
## Kali Linux 2 Fixer v 0.16		##
## By Nathan ASH 					##
## http://nathanash.id.au 			##
## https://github.com/ompster		##
## @ompster 						##
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
	os.system ('apt-get -y chromium')
	exit()

def install_xfce_func :
	print 'We are about to download the XFCE4 and plugins...'
	os.system ('apt-get -y install kali-defaults kali-root-login desktop-base xfce4 xfce4-places-plugin xfce4-goodies')
	default_xfce = raw_input 'Would you like to make XFCE your default desktop-enviroment? Y/N'
	default_xfce = default_xfce.upper()

	if default_xfce == 'Y' :
		print 'We will now install SLIM login manager and make XFCE the default desktop-enviroment...'
		os.system ('apt-get -y install slim')
		os.system ('mv .xinitrc ~/.xinitrc')
		print 'All done! You need to reboot for changes to take effect :)'
		print 'We will rebot now...'
		raw_input 'Press Enter....'
		os.system ('reboot')
		exit()

print '''
KALI FIXER 2                                               
	'''
print '''
		What would you like to do?
		1. Fix armitage
		2. Install Chrome
		3. Install XFCE4
		4. Exit
		'''
menu_option = raw_input('-> ')

if menu_option == "1" :
	fix_armitage_func()
elif menu_option == "2" :
	install_chrome_func()
elif menu_option == "3"
else :
	print '''
	http://github.com/ompster
	@ompster                      
	'''

	exit()




