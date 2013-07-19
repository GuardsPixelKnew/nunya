#!/usr/bin/env python

"""
The idea here is that the user has an account on multiple servers.
We should allow the user to move files from the local machine to any of the servers.
We should also allow the user to move files from any of the servers to each other.
The application will use local credentials only. No login password unless required by the ssh key.
The app needs to recognize only those files and folders where the user has permissions.
"""


# Retrieve credentials
	#Get ssh key

# Load list of saved friendly servers

# Get ssh connection to all BBB servers in list

# How do we know what the user can access?
# This list needs to be maintained on the server itself and retrieved by this application
	# Highest level dir of a dir vector where the user has user or group permissions
	# All dir where the user has permissions but does not have permissions up or down - isolated dirs
	# All files where the user has permissions but does not have dir permissions

# Retrieve base dirs and files from each server

# Display file manager listing all base dirs and single files

# All normal file manager functions on the files
	# Consider using one of these frameworks:
		# Fabric - https://pypi.python.org/pypi/Fabric
		# Paramiko - https://github.com/paramiko/paramiko
			# Leaning toward Paramiko...

# Requirements:
	# Python Modules:
		'''
		fabric
		paramiko
		pycrypto
		'''

	# Other:

#Functions

#Debugging

	#Set up a debugging mode for use outside of the current connection
	#Requires a current connection with root level privileges or via
	#an account with sudo privileges.

	#Start a new debugging server

	#Exit debugging server

	#Set CURRENT_SERVER to debugging server

	#Write banner file at /etc/ssh/ssh-banner
	#Set banner to: Banner /etc/ssh/ssh-banner

#Set protocol to: Protocol 2

#Changes to /etc/resolv.conf
	#Add lines desired

#Known hosts
	#update /etc/ssh/known_hosts - 
	#update $HOME/.ssh/known_hosts -  
	#update /etc/ssh/ssh_known_hosts -

	#verify known hosts

	#revoke known hosts keys

	#PuTTY uses the kh2reg.py program to convert hostkeys for its use
	#This utility is only found with the PuTTY source code in the 
	#contrib directory.
	#This utility makes a .reg file that must be installed.


#Create server keys / Nation keys

#Create user keys 
#Distribute public user keys
	#$HOME/.ssh/authorized_keys - keys to allow, should be chmod 600
	#$HOME/.ssh/id_rsa.pub - default key to use
	#PuTTY .ppk file contains both public and private keys

	#review keys
	#add comments

#Agent forwarding - used to transfer files from one nation to another
#without using the local machine as an intermediary
#The only safe way to do this is to use your nation as the intermediary.
#The risk is that transfering files from a nation where you are a citizen 
#but not the ruler opens up use of your private key to the rulers (or anyone
#with root priveleges) of those nations.
#All files should be copied from one nation to your nation and then to another
#nation if necessary.
#TODO: consider this use and how it could be misused.
	#$SHH_AUTH_SOCK

#Port forwarding
	#/etc/hosts
	#C:\Windows\System32\drivers\etc\hosts
	#Set up local forwarding 
		#- what server, what ports, what direction, 
		#Might generate errors with already bound ports

#