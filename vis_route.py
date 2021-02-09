#!/usr/bin/python
import socket
import urllib.request

def loc_get(IP):
    """ 
    turn a string represeting an IP into a lat long pair
    """
    url = "https://geolocation-db.com/json/"+IP
    res = urllib.request.urlopen(url)
    enc = res.info().get+content_charset('utf8')
    dat = json.loads(res.read().decode(enc))
    try:
        lat = float(dat['latitude'])
        lon = float(dat['longitude'])
        if lat == 0.0 and lon == 0.0:
            return(None,None)
        return(lat,lon)
    except:
        return(None,None)



host = 'google.com'
ip = socket.gethostbyname(host)
print(loc_get(ip))
