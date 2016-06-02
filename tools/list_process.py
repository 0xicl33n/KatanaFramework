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
