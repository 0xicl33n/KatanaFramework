#!/usr/bin/python
from os import system as sysc
class TOOL:
	self.author = "0xicl33n"
	self.description = "Update Kali Linux"
	def __main__:
		print "This tool will update kali-rolling"
sysc('sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get clean && sudo apt-get dist-upgrade -y')