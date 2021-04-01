import urllib.request as url
import time

url.urlopen("http://192.168.43.38/?r1on")
time.sleep(1)
url.urlopen("http://192.168.43.38/?r1off")