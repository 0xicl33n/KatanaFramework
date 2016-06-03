#!/usr/bin/env python
from os import system as sysc
import random
import sys, re, optparse
random.seed(1337)

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
class TOOL:
	self.author = "0xicl33n"
	self.description = "Change mac"
	def __main__:
		print "Change mac for specified interface"

def randomMAC():
	mac = [ 0x00, 0x16, 0x3e,
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
	return ':'.join(map(lambda x: "%02x" % x, mac))

first_re = re.compile(r'^\d{3}$')
parser = optparse.OptionParser()
parser.set_defaults(random=False,specific_mac=False)
parser.add_option('-R', action='store_true', dest='random')
parser.add_option('-M', action='store_true', dest='specific_mac')
parser.add_option('--help', action='store_true',dest='print_help')
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

if options.print_help:
	print '''
	Changemac - change mac for interface
	
	Options:
		 -R will use a random mac for specified interface
		 -M will use a mac specified by the user
	
	Example:

	ktf.tool -t changemac -R wlan1
	ktf.tool -t changemac -M 00:00:00:00:00 wlan1
	'''
intf = sys.argv[3]

def run(choice):
	sysc('sudo airmon-ng check kill')
	sysc('sudo ifconfig %s down') % intf
	sysc('sudo ifconfig %s hw ether %s') %intf %choice
	sysc('sudo ifconfig %s up') %intf 

if options.random:
	r_mac = randomMAC()
	run(r_mac)

if options.specific_mac:
	run(specific_mac)