#!/usr/bin/env python
# This Tool requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from os import system as sysc
# END LIBRARIES 
class init:
	
	Author      = "0xicl33n"
	Description = "Restart networking"
	var         = {}
	Arguments   = {}
sysc('sudo networking restart')