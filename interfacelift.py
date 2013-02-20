#!/usr/bin/env python
import os
import urllib2
import re
import signal
import sys

url       = 'http://interfacelift.com/wallpaper/downloads/date/hdtv/1080p/'
useragent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'
pattern   = '(?<=<a href=")/wallpaper/.*jpg(?=">)' # The regex pattern used. Check the README

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

# add event handler to catch CTRL+C event and abort downloading
signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) > 1:
    directory = sys.argv[1]
    count     = 1
    while count < 999999:
            os.system('wget -P /tmp/ -nc -U "' + useragent + '" ' + url+"index"+str(count)+".html")
            data = open('/tmp/index'+str(count)+".html", 'r').read()
            pictures   = re.findall(pattern, data)
            urlcount   = len(pictures)
            for picture in pictures:
                    s = picture.replace('_', '/').split('/')
                    if os.path.exists(directory+s[3]+"_"+s[4]+"_"+s[5]):
                            print 'Found file already...'
                            #linkurl = "http://interfacelift.com/wallpaper/details/"+s[3]+"/"+s[4]+".html"
                            #os.system('jhead -cl "' + linkurl + '" '+directory+s[3]+"_"+s[4]+"_"+s[5])
                    else:
                        os.system('wget -P ' + directory + ' -nc -U "' + useragent + '" ' + 'http://interfacelift.com' + picture)
                        linkurl = "http://interfacelift.com/wallpaper/details/"+s[3]+"/"+s[4]+".html"
                        os.system('jhead -cl "' + linkurl + '" '+directory+s[3]+"_"+s[4]+"_"+s[5])
            if urlcount == 0:
                    quit()
            count += 1
            os.system('rm -rf /tmp/index'+str(count)+".html")
else:
    print "Usage: interfacelift.py <PathToStoreWallpapers>"
