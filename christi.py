#!/usr/bin/python3
"""
==============================================================================================================================
=   This script assumes the seedfile has been filled out in the following format                                             =
=   $keyfile = "D:\\PortErr_Logs\\Scripts\\id_dsa_Putty.ppk"                                                                 =
=   $ip;$name;$switchfabric;$switchprincipal;$user;$pw;$device,$portorbladeinfo                                              =
=   $ip = ip of the device                                                                                                   =
=   $name = name of device                                                                                                   =
=   $switchfabric = if the device is a SAN switch, what fabric is it in                                                      =
=   $switchprincipal = if the device is a SAN switch, is it the principal switch <(y/n)>                                     =
=   $user = user name to log in                                                                                              =
=   $pw = admin if really, really necessary                                                                                  =
=   $device = <sw for switch>, <stg for storage>,<NA* for devices that don't work either for login issues or other issues>   =
=   $portorbladeinfo = <blade = 1-5,8-12> <port = 0-47 or 1_15,1200_1215> or storage device like SVC or Isilon               =
=                                                                                                                            =
=   seedfile example for switch with blades                                                                                  =
=    $keyfile = "/home/CHALITTLE-P/.ssh/id_dsa.pub"                                                                          =
=    $switchip;$switchname;$switchfabric;$switchprincipal;$user;$pw;$device,$portorbladeinfo                                 =
=    10.10.36.14;sea-dcx03;PRODUCTION_CONFIG_A;Y;chalittle;password!;sw;3-4,7-9                                              =
=                                                                                                                            =
=   seedfile example for switch without blades                                                                               =
=    $keyfile = "/home/CHALITTLE-P/.ssh/id_dsa.pub"                                                                          =
=    $switchip;$switchname;$switchfabric;$switchprincipal;$user;$pw;$device,$portorbladeinfo                                 =
=    10.10.36.14;sea-dcx03;PRODUCTION_CONFIG_A;Y;chalittle;password!;sw;0-47                                                 =
=                                                                                                                            =
=   10.10.36.14;sea-dcx03;PRODUCTION_CONFIG_A;Y;chalittle;password1!;sw;1-5,8-12                                             =
=   10.191.19.21;den4s6vbdcxi01;DISASTER_RECOVERY_CONFIG_A;Y;chalittle;password1!;NAsw;                                      =
==============================================================================================================================

#############################################################################################
#                                                                                           #
#  Name:        Brocade_Stats_Clear.py                                                      #
#                                                                                           #
#  Purpose:     Script needs to:                                                            #
#               	1) Open the seedfile                                                    #
#               	2) ssh into each Brocade switch                                         #
#               	3) Parse seedfile to put the blade/port info in $portorbladeinfo        #
#               	4) Run portstatsclear -s <blades> or portstatsclear -i <ports>          #
#               	5) Run statsclear on the switch                                         #
#               	6) Run slotstatsclear                                                   #
#               	7) Added a task to run other commands if necessary                      #
#                                                                                           #
#  Parameters:  Please see above for the seed file format                                   #
#                                                                                           #
#  Author:      Christi Little                                                              #
#                                                                                           #
#  Date:        April 14, 2021                                                              #
# ----------------------------------------------------------------------------              #
#  Change Log:                                                                              #
# ----------------------------------------------------------------------------              #
#  Date         Change                                                                      #
#                                                                                           #
#  04/14/2020   Creation                                                                    #
#                                                                                           #
#############################################################################################
"""


#Imported Modules
# import os
# import sys
# import time
# import logging
# import threading
from os import walk
from pathlib import Path
from csv import DictReader, reader


global seedfile
global path
global publicKey

path = '/home/CHALITTLE/scripts/'
seedfile = "Davita_Test_SeedFile.txt"

#############################################
#           Reuseable Functions             #
#############################################


# Find the seed file in a directory
def find(file_to_find, path_to_search):
    # Import the path function as this allows us to check for a file
    # so we are not actually scanning a directory for the file, we are looking
    # for it definitivley
    the_file_i_want_to_find = Path(path_to_search + file_to_find)
    # Now we check to see if the source file exists
    if the_file_i_want_to_find.exists():
        #I have foudn it so I am returning it
        return the_file_i_want_to_find
    else:
        return None


#############################################
#           Main Functions                  #
#############################################
def main():
    thefile = find(seedfile, path)
    if thefile is None:
        print('Unable to find the Seedfile {}'.format(seedfile))
    else:
        # I have found the file so now to process it

        # open file in read mode
        seedData = open(thefile, 'r')
        # I am opening the file and skipping the first two lines to
        # get to the data
        switchData = seedData.readlines()[2:]
        # pass the file object to DictReader() to get the DictReader object
        for row in switchData:
            # row variable is a dictionary that represents a row in csv
            print(row.split(';'))

            for rowValue in row.split(';'):
                print(rowValue)

    # This is another way to walk a directory looking for files
    # onlyfiles = []
    # for (dirpath, dirnames, filenames) in walk(path):
    #     onlyfiles.extend(filenames)
    #     break
    # print(onlyfiles)


#############################################
#           Main Functions                  #
#############################################
#============================================
main()
#============================================
