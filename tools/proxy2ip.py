#!/usr/bin/env python
# This Tool requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
from core.Function import checkDevice #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
import subprocess
from os import system as sysc
# END LIBRARIES

class init:
	
	Author      = "0xicl33n"
	Description = "Connect through socks proxy to specific target ip"
	var         = {}
	Arguments   = {
		'p':[False ,'port'],
		'i':[False , 'interface'],
		'o':[False , 'target ip'],
		'c':[False , 'clean current iptables rules']
		'r':[False ,'restore default iptables']
		'h:':[True , 'print help']
		't':[False, 'start tor']
	}

def startTOR():
	sysc('service tor start')

def restoreiptables():

def showhelp():

def savedefaultrules():
	subprocess.Popen('if [ -f /etc/iptables.original ] ; then exit ; else service iptables stop && iptables-save > /etc/iptables.original && service iptables start ; fi',stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	print '[!] Original Iptables backed up'

def cleanIptables():
	sysc('iptables-save | awk '/^[*]/ { print $1 } 
                     /^:[A-Z]+ [^-]/ { print $1 " ACCEPT" ; }
                     /COMMIT/ { print $0; }' | iptables-restore')

def prox2ip(target,interface,port):
	subprocess.Popen('iptables -t nat -A OUTPUT ! -d %s/32 -o %s -p tcp -m tcp -j REDIRECT --to-ports %s',stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait() %target,interface,port
	subprocess.Popen('iptables -t nat -A OUTPUT -o %s -p udp -m udp --dport 53 -j REDIRECT --to-ports 1053',stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait() %interface
	subprocess.Popen('python $PWD/lib/pr0cks/pr0cks.py --proxy SOCKS5:127.0.0.1:%s',stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait() %port


def Main():
	savedefaultrules()
	if init.var['t'] == "enable":
		startTOR()
	if init.var['r'] == "enable":
		restoreiptables()
	if init.var['c'] == "enable":
		cleanIptables()
	if checkDevice(init.var['i']):
		if init.var['p'] == "enable" and if init.var['o'] == "enable":
			p0rt = init.var['p']
			host = init.var['o']
			intf = init.var['i']
			prox2ip(host,port,ip)
	else:
		showhelp()







