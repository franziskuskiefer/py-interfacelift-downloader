#!/usr/bin/env python

from urllib2 import urlopen
from re import findall
from subprocess import call
from os.path import expanduser

# Modify the two strings below to your preferences
urlspec   = 'rating/widescreen/1920x1200/'
directory = expanduser('~')+'/Pictures/Interfacelift'

urlbase   = 'http://interfacelift.com/wallpaper/'
pattern   = '(?<=<a href="/wallpaper/).*jpg(?=">)'
useragent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'
url       = urlbase+'downloads/'+urlspec
wgetcmd   = [ 'wget', '-U', useragent, '-P', directory, '-nc', '--wait=5', '--random-wait', '--limit-rate=100K', '--retry-connrefused', '--referer=http://www.interfacelift.com/wallpaper/' ]

pictures = []
for count in range(1,2):
        data = urlopen(url + "index" + str(count) + ".html").read()
        temp = findall(pattern, data)
        pictures += [urlbase+i for i in temp]
if len(pictures) > 0:
        print "Attempting to download", len(pictures), "files with wget..."
        call(wgetcmd+pictures)
        print "Complete."
else:
        print "No pictures to download. Either the range is zero in length or the regex needs to be refined."

# vim:sw=8:ts=8:et:sts=8
