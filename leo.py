import itchat
import urllib, json
url = "http://free.currencyconverterapi.com/api/v5/convert?q=cad_cny&compact=y"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data
print data['CAD_CNY']['val']
itchat.auto_login(enableCmdQR=2,hotReload=True)
url = 'http://image.sinajs.cn/newchart/v5/forex/k/day/CADCNY.gif'
itchat.send_image(url, toUserName='filehelper')


