import urllib
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=false
ctx.verify_mode=ssl.CERT_NONE

link=input("enter url:")
count=int(input("enter count:"))
pos=int(input("enter position:"))

print("retrieving: ",link)
for i in range(0,count):
    html=urllib.urlopen(link).read()
    soup=BeautifulSoup(html)
    tags=soup('a')

    link=tags[pos-1].get('href')

result=tags[pos-1].contents[0]
print(result)
