# -*- coding: UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import time
import re
if __name__ == "__main__":
    #1. Open the url by urllib
    req = request.Request("https://blog.csdn.net/weixin_40341116")
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
    response = request.urlopen(req)
    #2. Receive the response
    html = response.read()
    #3. Decode to fromat a human readable heml string
    html = html.decode("utf-8")
    #4. Parser the string 
    soup = BeautifulSoup(html,"html.parser")
    #5. According to view the source file of the aim page in firefox,
    #We have known that the aim node is named <dd> node, and the node
    #have a attribute named "title", the aim value is the value of <dd>
    #So firstly, we find all dd node
    dds = soup.find_all(re.compile("^dd"))
    for dd in dds:
        #Secondly, find the first node that have attributes
        if dd.attrs:
          #Get the value by key
          str1 = dd.attrs["title"]
          #Get current time
          timestr = time.strftime('%Y-%m-%d',time.localtime(time.time()))
          #6. Open file and save value
          with open(r'/home/junweigu/csdn-pv/data/pv_day.txt', 'a+') as f:
            f.write(timestr + ", " + str1 + '\n')
          #7. Stop
          break
