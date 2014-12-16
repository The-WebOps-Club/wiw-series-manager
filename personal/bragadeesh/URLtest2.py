import urllib2
req = urllib2.Request('https://www.facebook.com')
response = urllib2.urlopen(req)
page = response.read()
print "Start"
fobject = open('MyGoogle.html','w')
fobject.write(page)
fobject.close()
print "Stop"
