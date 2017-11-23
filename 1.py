import cookielib
import urllib2
import json
import time

time.
cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
req = urllib2.Request("http://zhiyou.smzdm.com/user/checkin/jsonp_checkin")
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#opener.addheaders=[('Host','zhiyou.smzdm.com')]
opener.addheaders=[('Referer','http://www.smzdm.com/'),('Host','zhiyou.smzdm.com')]
response = opener.open(req)

print response.read()
print type(response.read())
print json.loads(response.read())
#print response.read().json()['error']
#texts=json.loads(response.read())
#print type(texts)