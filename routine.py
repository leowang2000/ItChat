# This Python file uses the following encoding: utf-8
import itchat
import time
import requests
import datetime

itchat.auto_login(hotReload=True,enableCmdQR=2)
i=1
while i > 0:
    
    friendList = itchat.get_friends(update=True)[1:]
    t= datetime.datetime.now()
    hr=str(t.hour)
    m=str(t.minute)
    # itchat.send('Hello, filehelper'+hr+':'+m, toUserName='filehelper')

    if m=="42" :
        itchat.send('Hello, filehelper'+hr+':'+m, toUserName='filehelper')
    time.sleep(1) 
