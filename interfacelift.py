#!/usr/bin/env python
import os
import urllib2
import re

url       = 'http://interfacelift.com/wallpaper/downloads/date/hdtv/1080p/'
directory = '~'
useragent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'
pattern   = '(?<=<a href=")/wallpaper/.*jpg(?=">)' # The regex pattern used. Check the README
wgetoptions = " --wait=5 --random-wait --limit-rate=100K --retry-connrefused --referer=http://interfacelift.com/ "

pictures = []
count     = 1
while count < 2:
        data = urllib2.urlopen(url + "index" + str(count) + ".html").read()
        pictures += re.findall(pattern, data)
        count += 1
if len(pictures) > 0:
        print "Attempting to download", len(pictures), "files with wget..."
        os.system('wget -P ' + directory + ' -nc -U "' + useragent + '" ' + wgetoptions + ' -- ' + " http://interfacelift.com".join(pictures))
        print "Complete."
else:
        print "No pictures to download"
