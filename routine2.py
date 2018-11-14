# This Python file uses the following encoding: utf-8
import itchat
import time
import requests
import datetime

itchat.auto_login(hotReload=True,enableCmdQR=2)
i=1
while i > 0:
    
    friendList = itchat.get_friends(update=True)[1:]
    chatrooms = itchat.get_chatrooms(update=True)
    t= datetime.datetime.now()
    hr=str(t.hour)
    m=str(t.minute)
    # itchat.send('Hello, filehelper'+hr+':'+m, toUserName='filehelper')

    if m=="42" and hr=="16":
        itchat.send('Hello, filehelper'+hr+':'+m, toUserName='filehelper')
        url = 'http://image.sinajs.cn/newchart/v5/forex/k/day/CADCNY.gif'
        filename = url.split('/')[-1]
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
        itchat.send_image(filename,toUserName='filehelper')
        for chatroom in chatrooms:
            print j
            j=j+1
            if chatroom['NickName'].find(u'亲友') > -1:
                print chatroom['UserName']
                print chatroom['NickName']
                itchat.send_image(filename,chatroom['UserName'])

    time.sleep(31) 
