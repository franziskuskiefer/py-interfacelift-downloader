#!/usr/bin/env python
import os
import urllib2
import re
import signal
import sys

url       = 'http://interfacelift.com/wallpaper/downloads/date/hdtv/1080p/'
directory = '/datapool/public/wallpaper/1080p'
useragent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'
pattern   = '(?<=<a href=")/wallpaper/.*jpg(?=">)' # The regex pattern used. Check the README

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

# add event handler to catch CTRL+C event and abort downloading
signal.signal(signal.SIGINT, signal_handler)

count     = 1
while count < 999999:
        data       = urllib2.urlopen(url + "index" + str(count) + ".html").read()
        pictures   = re.findall(pattern, data)
        urlcount   = len(pictures)
        for picture in pictures:
                if os.path.exists(directory + picture):
                        print 'Directory up to date. Found existing file.'
                        quit()
                os.system('wget -P ' + directory + ' -nc -U "' + useragent + '" ' + 'http://interfacelift.com' + picture)
        if urlcount == 0:
                quit()
        count += 1
