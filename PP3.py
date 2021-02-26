import os
import re
import collections
from urllib.request import urlretrieve


URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
#This code opens the access log files 
fileh = open ('local_copy.log', "r")
#This code will get each line into a element to a list from the log file.

TOTAL = 0
YEAR = 0

o = open (LOCAL_FILE)
for line in o:
    if "1995" in line:
        YEAR += 1
    print ("Request from 1995: " , YEAR)    

def file_len(local_file):
    with open (LOCAL_FILE) as f:
        for i, l in enumerate (f):
            pass
        return i + 1
print ("Request Made")
print(file_len(LOCAL_FILE))


#def yearlyResponses(local_file):
    #with open (LOCAL_FILE) as h:
        #for line in fileh:
            #items = line.splitlines ()
            #if len(items) < 9:
               # continue
            #year = items[3].splitlines(':')[0][-4]
            #if year == '1995':
             #   YEAR += 1
            #TOTAL += 1
#print("Request made in last year: "