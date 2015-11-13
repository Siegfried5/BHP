import urllib2

url = "http://192.168.130.133"

headers={}
headers['User-Agent'] = "Googlebot"

request = urllib2.Request(url,headers=headers)
responces = urllib2.urlopen(request)

print responces.read()
responces.close()
