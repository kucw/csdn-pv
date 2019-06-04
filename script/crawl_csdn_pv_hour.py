# -*- coding: UTF-8 -*-
# use python3
import requests
from bs4 import BeautifulSoup
import time
import re
import os
if __name__ == "__main__":
    #1. Set url
    url = "https://blog.csdn.net/weixin_40341116"
    #2. Receive the response
    res = requests.get(url)
    #3. Decode to fromat a human readable heml string
    res.encoding = 'utf-8'
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
            timestr = time.strftime('%H',time.localtime(time.time()))
            daystr = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            monthstr = time.strftime('%Y-%m',time.localtime(time.time()))
            #6. Open file and save value
            if not os.path.exists('/home/junweigu/csdn-pv/data/' + monthstr):
                os.makedirs('/home/junweigu/csdn-pv/data/' + monthstr)
            with open(r'/home/junweigu/csdn-pv/data/' + monthstr + '/pv_hour.' + daystr + '.txt', 'a+') as f:
                f.write(timestr + "," + str1 + '\n')
            #7. Stop
            break
