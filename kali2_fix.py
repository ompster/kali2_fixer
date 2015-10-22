######################################
## Kali Linux 2 Fixer v 0.16		##
## By Nathan ASH 					##
## http://nathanash.id.au 			##
## https://github.com/ompster		##
## @ompster 						##
######################################
from tempfile import mkstemp
from shutil import move
from os import remove
import subprocess
import os

import sys

########## file write functions #########
def func_append_file(appendFile, appendText):
	with open(appendFile, "a") as appendFile:
		appendFile.write(appendText)

def replace(source_file_path, pattern, substring):
    fh, target_file_path = mkstemp()
    with open(target_file_path, 'w') as target_file:
        with open(source_file_path, 'r') as source_file:
            for line in source_file:
                target_file.write(line.replace(pattern, substring))
    remove(source_file_path)
    move(target_file_path, source_file_path)
##########################################

print '''
>=>   >=>         >>       >=>       >=>            >=======> >=> >=>      >=> >=======> >======>     
>=>  >=>         >>=>      >=>       >=>   >=>>=>   >=>       >=>  >=>   >=>   >=>       >=>    >=>   
>=> >=>         >> >=>     >=>       >=>  >>   >=>  >=>       >=>   >=> >=>    >=>       >=>    >=>   
>>=>>          >=>  >=>    >=>       >=>      >=>   >=====>   >=>     >=>      >=====>   >> >==>      
>=>  >=>      >=====>>=>   >=>       >=>     >=>    >=>       >=>   >=> >=>    >=>       >=>  >=>     
>=>   >=>    >=>      >=>  >=>       >=>   >=>      >=>       >=>  >=>   >=>   >=>       >=>    >=>   
>=>     >=> >=>        >=> >=======> >=>  >======>  >=>       >=> >=>      >=> >=======> >=>      >=> 	
	'''



def func_dvwa_install():
	print 'This will install damn vulnerable web app for you to practice on.'
	print 'The installer will download the site files for you....'
	os.system('git clone https://github.com/randomstorm/DVWA.git')
	os.system('mv DVWA /var/www/html')
	print 'Changing DVWA database configs'
	replace('/var/www/html/DVWA/config/config.inc.php','p@ssw0rd','')
	os.system('chmod 664 /var/www/html/DVWA/config/config.inc.php')
	print 'Install complete.....'
	print 'Starting apache2 and mysql service for you now...'
	os.system('service apache2 start')
	os.system('service mysql start')
	print 'Lets launch it to test!'
	print 'You will need to click install on the webpage to create the database ,etc'
	os.system('clear')
	print 'You will need to click create Database at the bottom of the page, you should then be redirected to the login page'
	print 'Default credentials are:'
	print 'admin'
	print 'password'
	os.system('firefox http://localhost/DVWA')
	func_menu()



def func_install_vbox():
	print 'Add VirtualBox sources and signing key then update source list...'
	func_append_file('/etc/apt/sources.list', 'deb http://download.virtualbox.org/virtualbox/debian vivid contrib')
	os.system('wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -')
	os.system('apt-get -y update')
	print 'now install VirtualBox 5.0'
	os.system('apt-get install -y virtualbox-5.0')
	print 'We are all done! lets launch it!'
	os.system('virtualbox')
	func_menu()



def func_install_linset():
	print 'We are about to install linset. First I will clone the github repo then install all the required tools...'
	os.system('git clone https://github.com/Trig0n/Linset.git /usr/bin/linset')
	print 'Have to make sure kali sources are up to date so i will do that now....'
	os.system('apt-get update')
	os.system('apt-get install -y isc-dhcp-server Hostapd dnsmasq lighttpd php5-cgi')
	print 'writing permissions....'
	subprocess.call(['chmod', 'u+x', '/usr/bin/linset/linset'])
	os.system('clear')
	print 'Install Complete! we will run linset now to test!'
	subprocess.call(['/usr/bin/linset/linset'])
	func_menu()


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
		print 'thanks for using! - @ompster'
		func_menu()
	####END FIX ARMITAGE####

def install_chrome_func() :
	print 'Installing Chromium, will first update sources...'
	os.system ('apt-get update')
	os.system ('apt-get -y install chromium')
	func_menu()

def install_xfce_func() :
	print 'We are about to download the XFCE4 and plugins...'
	os.system ('apt-get -y install kali-defaults kali-root-login desktop-base xfce4 xfce4-places-plugin xfce4-goodies')
	default_xfce = raw_input ('Would you like to make XFCE your default desktop-enviroment? Y/N')
	default_xfce = default_xfce.upper()

	if default_xfce == 'Y' :
		print 'We will now install SLIM login manager and make XFCE the default desktop-enviroment...'
		os.system ('clear')
		print 'IN THE NEXT SCREEN YOU SHOULD SELECT SLIM AS THE DEFAULT LOGIN MANAGER!'
		raw_input ('Press Enter to continue...')
		os.system ('apt-get install -y slim')
		os.system ('mv .xinitrc ~/.xinitrc')
		os.system ('clear')
		print 'All done! You need to reboot for changes to take effect :)'
		print 'We will rebot now...'
		raw_input ('Press Enter....')

def func_menu() :
	print '''
	>=>   >=>         >>       >=>       >=>            >=======> >=> >=>      >=> >=======> >======>     
	>=>  >=>         >>=>      >=>       >=>   >=>>=>   >=>       >=>  >=>   >=>   >=>       >=>    >=>   
	>=> >=>         >> >=>     >=>       >=>  >>   >=>  >=>       >=>   >=> >=>    >=>       >=>    >=>   
	>>=>>          >=>  >=>    >=>       >=>      >=>   >=====>   >=>     >=>      >=====>   >> >==>      
	>=>  >=>      >=====>>=>   >=>       >=>     >=>    >=>       >=>   >=> >=>    >=>       >=>  >=>     
	>=>   >=>    >=>      >=>  >=>       >=>   >=>      >=>       >=>  >=>   >=>   >=>       >=>    >=>   
	>=>     >=> >=>        >=> >=======> >=>  >======>  >=>       >=> >=>      >=> >=======> >=>      >=> 	
		'''
	print '''
			What would you like to do?
			1. Fix armitage
			2. Install Chrome
			3. Install XFCE4
			4. Install Linset (Evil-twin WPA attack)
			5. Install VirtualBox
			6. Install Damn Vulnerable Web App (DVWA)
			7. Update This Script
			0.Exit
			'''
	menu_option = raw_input('-> ')

	if menu_option == "1" :
		fix_armitage_func()
	elif menu_option == "2" :
		install_chrome_func()
	elif menu_option == "3" :
		install_xfce_func()
	elif menu_option == "4" :
		func_install_linset()
	elif menu_option == "5" :
		func_install_vbox()
	elif menu_option == "6" :
		func_dvwa_install()
	elif menu_option == "00" :
		print 'You are about to install everything! Hit enter to continue...'
		raw_input('......................................................')
		fix_armitage_func()
		install_chrome_func()
		install_xfce_func()
		func_install_linset()
		func_install_vbox()
		func_dvwa_install()
	else :
		print '''
		GOODBYE!
		http://github.com/ompster
		@ompster                      
		'''

		exit()

func_menu()


