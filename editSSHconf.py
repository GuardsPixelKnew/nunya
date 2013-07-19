#!/usr/bin/env python

#############################################################################
#  editSSHconf.py - description
#  Copyright (C) 2009 
# @author: Kevin Partridge
#
# 
#############################################################################

# Script was tested using Python 2.7


from ssh_configuration import *

#Read current file

lines = open("someFile", "r").read().splitlines()
IP = "10.10.1.10"
hostname = None
for i, line in enumerate(lines):
    if IP in line:
        hostname = lines[i - 1]
        break

if hostname:
    # Do stuff

#Save file as new backup file using current date as the extension
	#Name template: <current name>.BAK-<date>

#Skip comment lines
#Read in all lines until next "Host" line
#Check that "Host" line matches desired change domain
#Find line to change
	#Find the first occurrence of the search pattern
	#Collect lines until we encounter a line with 
	#a pattern for another setting
#
#Change line to desired line
#Show lines to be changed
#
#
#
#Add conditional match lines at the end
#
#Show lines to be written
#
#Write new file

if __name__ == '__main__':
	
