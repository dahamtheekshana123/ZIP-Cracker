# The Zip Password Cracker..
# Code By Imalsha Nethmina..

try:
	import zipfile
except :
	print (Color.BLUE+" [!] Can't Run Program..! [USE : pip install zipfile]"+Color.RESET)
import os
import time

class Color:
	YELLOW = '\033[93m'
	RED = '\033[91m'
	RESET = '\033[0m'
	BLUE = '\033[96m'
	dBLUE = '\033[94m'
	GREEN = '\033[92m'

def clear():
	os.system(["clear", "cls"][os.name == 'nt'])

def banner():
	print (Color.YELLOW+"\n ########################")
	print (" ###"+Color.RED+"___/**********\___"+Color.YELLOW+"###")
	print (" ##"+Color.RED+"|                  |"+Color.YELLOW+"##")
	print (" ##"+Color.RED+"|                  |"+Color.YELLOW+"##")
	print (" # "+Color.BLUE+"ZIP Password Cracker"+Color.YELLOW+" #")
	print (" ##"+Color.RED+"|                  |"+Color.YELLOW+"##")
	print (" ##"+Color.RED+"| ("+Color.BLUE+"made by,      "+Color.RED+") |"+Color.YELLOW+"##")
	print (" ##"+Color.RED+"| ("+Color.BLUE+"     Daham "+Color.RED+") |"+Color.YELLOW+"##")
	print (" ##"+Color.RED+"|___            ___|"+Color.YELLOW+"##")
	print (" ######"+Color.RED+"\**********/"+Color.YELLOW+"######")
	print (" ########################\n"+Color.RESET)

#Cracking...\\
def try_Crack():

	clear()
	banner()
	print (Color.YELLOW+" ["+Color.RED+"$"+Color.YELLOW+"]"+Color.BLUE+" Start Cracking"+Color.RED+"... ["+Color.GREEN+zipName+""+Color.RED+"]\n\n")
	time.sleep(3)
	found = False

	for password in WList:
		try:
			ZIP.extractall(pwd=password.strip().encode())
			print (Color.YELLOW+"\n ["+Color.RED+"$"+Color.YELLOW+"]"+Color.BLUE+" Password Found"+Color.RED+" ["+Color.GREEN+password.strip()+Color.RED+"]")
			print (Color.YELLOW+"\n ["+Color.RED+"!"+Color.YELLOW+"]"+Color.BLUE+" Thanks For Using"+Color.RED+"../ :)\n"+Color.RESET)
			input(Color.RED+" ["+Color.BLUE+"Exit"+Color.RED+"] "+Color.RESET)
			found = True
			exit()
		except:
			if found==False:
				print (Color.YELLOW+" ["+Color.RED+"!"+Color.YELLOW+"]"+Color.dBLUE+" Password Not Found "+Color.RED+"["+Color.BLUE+password.strip()+Color.RED+"] ")
	if found==False:
		print (Color.YELLOW+"\n ["+Color.RED+"!"+Color.YELLOW+"]"+Color.dBLUE+" Password Not Found This Wordlist"+Color.RED+"... ["+Color.GREEN+passName+Color.RED+"]")
		print (Color.YELLOW+"\n ["+Color.RED+"!"+Color.YELLOW+"]"+Color.BLUE+" Thanks For Using"+Color.RED+"../ :)\n"+Color.RESET)
		input(Color.RED+" ["+Color.BLUE+"Exit"+Color.RED+"] "+Color.RESET)
		exit()

#Start Menu..
clear()
banner()

print (Color.YELLOW+" ["+Color.RED+"1"+Color.YELLOW+"]"+Color.BLUE+" Start")
print (Color.YELLOW+" ["+Color.RED+"0"+Color.YELLOW+"]"+Color.BLUE+" Exit")

cho = input(Color.YELLOW+"\n ["+Color.RED+"?"+Color.YELLOW+"]"+Color.BLUE+" Chose Number "+Color.RED+": "+Color.BLUE) 
if cho == "0":
	clear()
	banner()
	print (Color.YELLOW+" ["+Color.RED+"!"+Color.YELLOW+"]"+Color.BLUE+" Thanks For Using"+Color.RED+"../ :)\n"+Color.RESET)
	input(Color.RED+" ["+Color.BLUE+"Exit"+Color.RED+"] "+Color.RESET)
	exit()
elif cho != "1":
	clear()
	banner()
	print (Color.YELLOW+" ["+Color.RED+"!"+Color.YELLOW+"] "+Color.dBLUE+""+cho+" "+Color.RED+"< "+Color.dBLUE+"Not Found"+Color.RED+"..! \n")
	print (Color.YELLOW+" ["+Color.RED+"!"+Color.YELLOW+"]"+Color.BLUE+" Thanks For Using"+Color.RED+"../ :)\n"+Color.RESET)
	input(Color.RED+" ["+Color.BLUE+"Exit"+Color.RED+"] "+Color.RESET)
	exit()

#Get Files..
clear()
banner()

zipName = input(Color.YELLOW+" ["+Color.RED+"+"+Color.YELLOW+"] "+Color.BLUE+"Enter ZIP File Path "+Color.RED+": "+Color.BLUE)
passName = input(Color.YELLOW+" ["+Color.RED+"+"+Color.YELLOW+"] "+Color.BLUE+"Enter Wordlist Path "+Color.RED+": "+Color.BLUE)

try:
	ZIP = zipfile.ZipFile(zipName)
except:
	print (Color.YELLOW+"\n ["+Color.RED+"!"+Color.YELLOW+"] "+Color.dBLUE+"Can't Load ZIP File"+Color.RED+"..!\n"+Color.RESET)
	input(Color.RED+" ["+Color.BLUE+"Exit"+Color.RED+"] "+Color.RESET)
	exit()

try:
	WList = open(passName, 'r').readlines()
except:
	print (Color.YELLOW+"\n ["+Color.RED+"!"+Color.YELLOW+"] "+Color.dBLUE+"Can't Load Wordlist"+Color.RED+"..!\n"+Color.RESET)
	input(Color.RED+" ["+Color.BLUE+"Exit"+Color.RED+"] "+Color.RESET)
	exit()

if cho == "1":
	try_Crack()
###################################################### TOOL IS END #######################################################
#################################################### THANKS FOR USING ####################################################
