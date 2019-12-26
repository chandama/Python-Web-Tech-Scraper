
#Script to scrape public DLP Tech articles
#Written by: Chandler Taylor
#Date: 12/26/2019
import sys
import requests
import time
import urllib2
import os
import errno
from lxml import html

#Declare list variable and read newline separated list of tech article numbers into array
techlist = list()

if sys.argv[2] is None:
    print "Missing output path"
else:
    filepath = sys.argv[2]

try:
    techlist = [line.rstrip('\n') for line in open(sys.argv[1])]
except NameError:
    print("Missing argument")

#Create copy of techlist to just store aritcle name and number
namelist = list(techlist)

#Take elements from techlist and create full URLs and scrape URL's into html
for i, val in enumerate(techlist):
    techlist[i] = 'https://support.symantec.com/us/en/article.' + techlist[i] + '.html'
    scrape = techlist[i]
    page = requests.get(scrape)
    new = page.content
    #Grab element from namelist to just grab TECH###### without URL
    if not os.path.exists(os.path.dirname(filepath)):
        try:
            os.makedirs(os.path.dirname(filepath))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    with open(filepath + namelist[i] + '.html', "w") as f:
        f.write(str(new)) 
    f.close()
