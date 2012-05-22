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
update=config.update
addon=config.addon
launcher=config.launcher


if update == "1":
	if addon == "yes":
		print("Update Addons")
		addoncheck = os.path.isfile('../Interface/AddOns/TrueWoWTicketMaster/TrueWoWTicketMaster.toc')
		if addoncheck == True:
			print("File is There")
			os.system('cd ../Interface/AddOns/TrueWoWTicketMaster && git pull -u')
		if addoncheck == False:
			print("File is NOT There. Creating")
			os.system('cd ../Interface/AddOns/ && git clone git://github.com/gamehacker953/TicketMaster.git TrueWoWTicketMaster')
	if launcher == "yes":
		print("Updating Launcher")
		os.system('git pull -u')
if update == "0":
	print("No Updates")
os.system("start realmlist.exe")