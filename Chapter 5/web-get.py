import urllib2

url = "http://furr.me/index.php"

headers={}
headers['User-Agent'] = "Googlebot"

request = urllib2.Request(url,headers=headers)
responces = urllib2.urlopen(request)

print responces.read()
responces.close()
