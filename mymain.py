import time
from ntptime import settime
from machine import Timer
import data
import mqtt
def mysettime(t):
    #获取网络时间及重试
    attempts = 0 
    success = False
    while attempts < 3 and not success:
      try:
        settime()
        success = True
      except:
        attempts += 1
        if attempts == 3:
          break  
        time.sleep(attempts *5)  

def main():
    #获取网络时间及重试
    time.sleep(30)
    mysettime(3)
    #因eps8266的时钟不准备，因此需要每3小时获取网络时间一次，校准
    timxs = Timer(-1)
    timxs.init(period=11558000, mode=Timer.PERIODIC, callback=mysettime)
    #mycontime=time.localtime()[3]
    #设置设备维护时间中午1点，可打开webrepl上传data.py，也可直接在data.py中直接设置BG=1，重启后打开维护状态
    if data.BG != 0:
      #if mycontime != 5:  #5+8为中国区
      #初始化三路定时器
      import kaiguanconfig
      kaiguanconfig.dinshi_config(10)
      kaiguanconfig.c1.begin()
      kaiguanconfig.c2.begin()
      kaiguanconfig.c3.begin()
      
      #开始联接中移动物联网
      product_id = data.Product_id
      regKey = data.Password
      clientId = data.Client_id
      server_ip=data.Server_ip
      mq = mqtt.mqtt(client_id=clientId, username=product_id, password=regKey, server=server_ip)
      mq.connect()
    else:
      pass      
main()