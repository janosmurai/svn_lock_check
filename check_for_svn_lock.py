# Python 2
# Author: janos.murai
import time
import os

path = raw_input("Path of the locked file: ")
script_path = os.path.dirname(os.path.abspath(__file__))
while True:
	os.system("svn info " + path + " > " + script_path + "/lock_info")
	f = open(script_path + "/lock_info")
	locked = False
	for line in f:
		if line.startswith("Lock Owner: "):
			locked = True
			break
	if not locked:
		os.system("notify-send \"Lock Info\" \""+ path + " is unlocked\"")
	else:
		print("locked!\n")
	f.close
	#Clean up the mess
	os.remove(script_path + "/lock_info")
	time.sleep(10)			
