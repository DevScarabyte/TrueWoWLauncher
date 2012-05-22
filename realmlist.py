import os.path
import sys
import imp
import time

def configFile(filename):
	f = open(filename)
	global config
	config = imp.load_source('config', '', f)
	f.close

configFile('config.ini')
realm='realmlist.wtf'
realm1=config.realm1
realm1name=config.realm1name
update=config.update
realm2=config.realm2
realm2name=config.realm2name
realm3=config.realm3
realm3name=config.realm3name
wow=config.wow
realmamount=config.realmamount
test="this is it"


if realmamount == "3":
	check1 = os.path.isfile(realm1)
	check2 = os.path.isfile(realm2)
	check3 = os.path.isfile(realm3)
	checkmain = os.path.isfile(patch)
	checkwow= os.path.isfile(wow)
	if check1 == True:
		if check2 == True:
			print '%s is current Server!' % (realm3name)
			if checkwow == True:
				print 'Wow.exe detected'
			if checkwow == False:
				print 'Wow.exe is not detected. rename WoW to Wow.exe (captial W)'
			change1 = raw_input("Press for options\n1 for {0} \n2 for {1}     \nN for No Change   \nOption>> ".format(realm1name, realm2name))
			if change1 == '1':
				os.rename(realm, realm3)
				os.rename(realm1, realm)
				checkmove = os.path.isfile(realm3)
				if checkmove == False:
					print 'Failed to move File!'
				if checkmove == True:
					print 'Completed Successfully!'
					print 'Starting WoW'
					os.system('start ../Wow.exe')
			if change1 == '2':
				os.rename(realm, realm3)
				os.rename(realm2, realm)
				checkmove = os.path.isfile(realm3)
				if checkmove == False:
					print 'Failed to move File!'
				if checkmove == True:
					print 'Completed Successfully!'
					print 'Starting WoW'
					os.system('start ../Wow.exe')
			if change1 == 'n':
				print 'Starting WoW'
				os.system('start ../Wow.exe')
		if check3 == True:
			print '%s is current Server!' % (realm2name)
			if checkwow == True:
				print 'Wow.exe detected'
			if checkwow == False:
				print 'Wow.exe is not detected. rename WoW to Wow.exe (captial W)'
			change1 = raw_input("Press for options\n1 for {0} \n2 for {1}  \nN for No Change   \nOption>> ".format(realm1name, realm3name))
			if change1 == '1':
				os.rename(realm, realm2)
				os.rename(realm1, realm)
				checktruewow = os.path.isfile(realm2)
				if checktruewow == False:
					print 'Failed to move File!'
				if checktruewow == True:
					print 'Completed Successfully!'
					print 'Starting WoW'
					os.system('start ../Wow.exe')
			if change1 == '2':
				os.rename(realm, realm2)
				os.rename(realm3, realm)
				checktruewow = os.path.isfile(realm2)
				if checktruewow == False:
					print 'Failed to move File!'
				if checktruewow == True:
					print 'Completed Successfully!'
					print 'Starting WoW'
					os.system('start ../Wow.exe')
			if change1 == 'n':
				print 'Starting WoW'
				os.system('start ../Wow.exe')
	if check2 == True:
		if check3 == True:
			print '%s is current Server!' % (realm1name)
			if checkwow == True:
				print 'Wow.exe detected'
			if checkwow == False:
				print 'Wow.exe is not detected. rename WoW to Wow.exe (captial W)'
			change1 = raw_input("Press for options\n1 for {0} |\n2 for {1} |\nN for No Change |\nOption>> ".format(realm2name, realm3name))
			if change1 == '1':
				os.rename(realm, realm1)
				os.rename(realm2, realm)
				checklocal = os.path.isfile(realm1)
				if checklocal == False:
					print 'Failed to move File!'
				if checklocal == True:
					print 'Completed Successfully!'
					print 'Starting WoW'
					os.system('start ../Wow.exe')
			if change1 == '2':
				os.rename(realm, realm1)
				os.rename(realm3, realm)
				checklocal = os.path.isfile(realm1)
				if checklocal == False:
					print 'Failed to move File!'
				if checklocal == True:
					print 'Completed Successfully!'
					print 'Starting WoW'
					os.system('start ../Wow.exe')
			if change1 == 'n':
				print 'Starting WoW'
				os.system('start ../Wow.exe')
if realmamount == "2":
	check = os.path.isfile(realm2)
	if check == True:
		print '%s is current Server!' % (realm1name)
		change1 = raw_input("Change to {0}? (y or n): ".format(realm2name))
		if change1 == 'y':
			os.rename(realm, realm1)
			os.rename(realm2, realm)
			checktruewow = os.path.isfile(realm1)
			if checktruewow == False:
				print 'Failed to move File!'
			if checktruewow == True:
				print 'Completed Successfully!'
				print 'Starting WoW'
				os.system('start ../Wow.exe')
		if change1 == 'n':
			print 'Starting WoW'
			os.system('start ../Wow.exe')
	if check == False:
		print '%s is Selected!' % (realm2name)
		change2 = raw_input("Change to {0}? (y or n): ".format(realm1name))
		if change2 == 'y':
			os.rename(realm, realm2)
			os.rename(realm1, realm)
			checkmove = os.path.isfile(realm2)
			if checkmove == False:
				print 'Failed to move File!'
			if checkmove == True:
				print 'Completed Successfully!'
				print 'Starting WoW'
				os.system('start ../Wow.exe')
		if change2 == 'n':
			print 'Starting WoW'
			os.system('start ../Wow.exe')
if realmamount == "1":
	os.system('start ../Wow.exe')
updatecheck=os.path.isfile('update1.exe')
if updatecheck == True:
	os.system('del update.exe')
	os.rename('update1.exe', 'update.exe')
time.sleep(5)
