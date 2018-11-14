# This Python file uses the following encoding: utf-8
import itchat
import time
import requests
import datetime
import json
import urllib
#itchat.auto_login(hotReload=True,enableCmdQR=2)
i=1
while i > 0:
    itchat.auto_login(hotReload=True,enableCmdQR=2) 
    #friendList = itchat.get_friends(update=True)[1:]
    chatrooms = itchat.get_chatrooms(update=True)
    t= datetime.datetime.now()
    hr=str(t.hour)
    m=str(t.minute)
    #itchat.send('Hello, filehelper'+hr+':'+m, toUserName='filehelper')

    if m=="5":
        url = "http://free.currencyconverterapi.com/api/v5/convert?q=cad_cny&compact=y"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print data
        print data['CAD_CNY']['val']
        itchat.send(u'当前加元汇率是'+str(data['CAD_CNY']['val']), toUserName='filehelper')
        url = 'http://image.sinajs.cn/newchart/v5/forex/k/day/CADCNY.gif'
        filename = url.split('/')[-1]
       # r = requests.get(url, allow_redirects=True)
       # open(filename, 'wb').write(r.content)
       # itchat.send_image(filename,toUserName='filehelper')
        for chatroom in chatrooms:
            #print j
            #j=j+1
            #if chatroom['NickName'].find(u'亲友') > -1:
            if chatroom['NickName'].find(u'鑫鑫') > -1:
               # print u'chatroom["UserName"]'
               # print u'chatroom["NickName"]'
                itchat.send(u'当前加元汇率是'+str(data['CAD_CNY']['val']), chatroom['UserName'])
               # itchat.send_image(filename,chatroom['UserName'])

    time.sleep(31) 
