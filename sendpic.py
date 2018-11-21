# This Python file uses the following encoding: utf-8
import itchat
import time
import requests
import datetime

itchat.auto_login(hotReload=True,enableCmdQR=2)
i=1
if 1==1:
    #friendList = itchat.get_friends(update=True)[1:]
    chatrooms = itchat.get_chatrooms(update=True)
    t= datetime.datetime.now()
    hr=str(t.hour)
    m=str(t.minute)
    # itchat.send('Hello, filehelper'+hr+':'+m, toUserName='filehelper')
    if 1==1:
        itchat.send('Hello, filehelper'+hr+':'+m, toUserName='filehelper')
       # url = 'https://media.apnarm.net.au/media/images/2013/09/13/9-13-2013_1-03-49_PM_fct475x358x108_ct677x380.png'
        url='https://media.gettyimages.com/photos/hispanic-school-crossing-guard-with-a-stop-sign-as-elementary-school-picture-id141856623'
        filename = url.split('/')[-1]
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
        itchat.send_image(filename,toUserName='filehelper')
        j=0
        for chatroom in chatrooms:
            print j
            j=j+1
            if chatroom['NickName'].find(u'山庄') > -1:
                print chatroom['UserName']
                print chatroom['NickName']
                itchat.send_image(filename,chatroom['UserName'])

