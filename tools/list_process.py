# This Tool requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: 
# Katana Core import                  
from core.KATANAFRAMEWORK import *
import sys    
try:
    from pydbg import *
    from pydbg.defines import *
    from utils import hooking
except:
    print "ERROR: you need pydbg and utils.hooking from PAIMEI."
    sys.exit(-1)
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: 

<<<<<<< HEAD
class TOOL:
	self.author = "0xicl33n"
	self.description = "List process"
	def __main__:
		print "This is a way to query running processes using pydgb. It is still a test"
dbg = pydbg()
def getProcess(name):
	name = y
	y = raw_input("What process to search for? (please specify .exe if on windows)>\t")
	for (pid, name) in dbg.enumerate_processes():
		x = name.lower()
		if x == y:
		#print '\n\n',x ,"is running"
		return x
=======
class init:
	
	Author      = "Redtoor"
	Description = "Test tool template"
	var         = {}
	Arguments   = {

		'i':[True ,'interface to change mac'],
		'm':[False,'specific mac'],
		'r':[True,'ramdom mac']
	}
	
def Main():
	print " ktf.tool -t list_process "
	print " ktf.tool -t list_process -h "
	print " ktf.tool -t list_process -i wlan0"
	print " ----------------------------------->error : -r is necesary"
	print " ktf.tool -t list_process -r"
	print " ----------------------------------->error : -r is empy and i is necesary"
	print " ktf.tool -t list_process -m -i wlan0 -r 232"
	print " ----------------------------------->good  : -m is enable, i is wlan0 , r is 232"
	print " ktf.tool -t list_process "

	print "interface "+init.var["i"]
	print "MAC       "+init.var["m"]
	print "ramdom    "+init.var["r"]
>>>>>>> upstream/master
