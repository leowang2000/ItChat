# This Python file uses the following encoding: utf-8
import itchat
import time
import requests
import datetime
import json
import urllib
itchat.auto_login(hotReload=True,enableCmdQR=2)
i=1
while i==1:
    #itchat.auto_login(hotReload=True,enableCmdQR=2) 
    #friendList = itchat.get_friends(update=True)[1:]
    chatrooms = itchat.get_chatrooms(update=True)
    t= datetime.datetime.now()
    hr=str(t.hour)
    m=str(t.minute)
    #itchat.send('Hello, filehelper'+hr+':'+m, toUserName='filehelper')
    i=i+1
    print i
    if m=='10' or  m=='35' or m=='50':
        url = 'http://free.currencyconverterapi.com/api/v5/convert?q=usd_cny&compact=y'
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        #print data
        ex=data['USD_CNY']['val']
        itchat.auto_login(hotReload=True,enableCmdQR=2)
        #itchat.send(u'当前加元汇率是'+str(data['CAD_CNY']['val']), toUserName='filehelper')
        url = 'http://image.sinajs.cn/newchart/v5/forex/k/day/CADCNY.gif'
        filename = url.split('/')[-1]
       # r = requests.get(url, allow_redirects=True)
       # open(filename, 'wb').write(r.content)
       # itchat.send_image(filename,toUserName='filehelper')
        j=0
        for chatroom in chatrooms:
            #print j
            j=j+1
            #if chatroom['NickName'].find(u'亲友') > -1:
            if chatroom['NickName'].find(u'test') > -1:
                print chatroom["UserName"].encode('utf-8')
                print chatroom["NickName"].encode('utf-8')
                itchat.send(u'USD汇率是'+str(ex), chatroom['UserName'])
                #itchat.send_image(filename,chatroom['UserName'])

