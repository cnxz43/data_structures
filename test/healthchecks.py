# -*- coding:utf-8 -*-

import pprint
# urllib with python 3.x:
import urllib.request

'''

https://hc-ping.com/484e7c9b-6f5f-4ce9-ab0c-7ab658f9584e



# Get a List of Existing Checks
https://healthchecks.io/api/v1/checks/?tag=foo&tag=bar

# Create a Check
POST https://healthchecks.io/api/v1/checks/



# gis
http://10.216.129.39:8080/gsystem/search/searchPoiList?keyword=%E5%B0%8F%E7%9F%B3%E5%AE%B6%E5%BA%84&page=1&pageSize=10&city=%E7%9F%B3%E5%AE%B6%E5%BA%84%E5%B8%82&county=%E6%99%8B%E5%B7%9E%E5%B8%82

'''
gisurl = 'http://10.216.129.39:8080/gsystem/search/searchPoiList?keyword=%E5%B0%8F%E7%9F%B3%E5%AE%B6%E5%BA%84&page=1&pageSize=10&city=%E7%9F%B3%E5%AE%B6%E5%BA%84%E5%B8%82&county=%E6%99%8B%E5%B7%9E%E5%B8%82'
# res = urllib.request.urlopen("https://hc-ping.com/484e7c9b-6f5f-4ce9-ab0c-7ab658f9584e")
# pprint.pprint(res)



import requests
URL = "https://hc-ping.com/your-uuid-here"

def do_work():
    # Do your number crunching, backup dumping, newsletter sending work here.
    # Return a truthy value on success.
    # Return a falsy value or throw an exception on failure.
    requests.get(gisurl)
    return True

success = False
try:
    success = do_work()
finally:
    # On success, requests https://hc-ping.com/your-uuid-here
    # On failure, requests https://hc-ping.com/your-uuid-here/fail
    res = requests.get(URL if success else URL + "/fail")

pprint.pprint(res)

