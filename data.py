#配置生效标志
BG = 1
#  Wifi配置
SSID ="NECK"
SSID_PASS="12345678aa"
# OneNet网络平台配置
Server_ip="183.230.40.39" #中移动平台IP
Client_id="aaaa"   #设备ID
Product_id="1ds489"   #产品ID
Password ="ddsfff6"    #注册KEY(Master-APIkey)或者是鉴权信息
Dinshi_config = [0,1,0] #默认温控启动常温设置
Dinshi_temp = [8,30]   #低于8度为低温，8－30为常温，大于30度为高温模式
#温控定时配置（三路）
Dinshi_data = \
    {0:{  #5度以下 
        'D1':{'zt':0,'xinhuan':172800,'kaishi':257,'yunxin':10,'norun':[16,17,18,19,20,21,22],'ykai':0},
                #第一路　喷淋 
                #48小时一次,257秒后开关1开启,持续运行10秒后关闭,夜间模式的时间8+小时,夜间模式下，0为全闭(不工作)
        'D2':{'zt':0,'xinhuan':3600,'kaishi':116,'yunxin':45,'norun':[14,15,16,17,18,19,20,21,22,23],'ykai':4},
                #第二路　风机 
                #60分钟一次,116秒后开关2开启,持续运行50秒后关闭,夜间模式的时间8+小时,夜间模式下，4次循环开一次
        'D3':{'zt':0,'xinhuan':28800,'kaishi':1625,'yunxin':2700,'norun':[99,100] ,'ykai':0}
                #第三路　造雾 
                #8小时一次,1625秒后开关3开启,持续运行0.75小时后关闭,夜间模式的时间8+小时本例为不设夜间模式,夜间模式下，0为全闭(不工作)
        },
    1:{  #5-10度
        'D1':{'zt':1,'xinhuan':129600,'kaishi':257,'yunxin':12,'norun':[16,17,18,19,20,21,22],'ykai':0},
        'D2':{'zt':1,'xinhuan':3300,'kaishi':15,'yunxin':45,'norun':[14,15,16,17,18,19,20,21,22,23],'ykai':3},
        'D3':{'zt':1,'xinhuan':28800,'kaishi':1625,'yunxin':2700,'norun':[99,100] ,'ykai':0}
      },
    2:{ #10-15度
        'D1':{'zt':2,'xinhuan':112320,'kaishi':257,'yunxin':15,'norun':[16,17,18,19,20,21,22],'ykai':0},
        'D2':{'zt':2,'xinhuan':3000,'kaishi':116,'yunxin':45,'norun':[14,15,16,17,18,19,20,21,22,23],'ykai':3},
        'D3':{'zt':2,'xinhuan':28800,'kaishi':1625,'yunxin':2700,'norun':[99,100] ,'ykai':0}
      },
    3:{ #15-20度
        'D1':{'zt':3,'xinhuan':64800,'kaishi':257,'yunxin':15,'norun':[16,17,18,19,20,21,22],'ykai':1},
        'D2':{'zt':3,'xinhuan':2400,'kaishi':116,'yunxin':45,'norun':[16,17,18,19,20,21,22,23],'ykai':2},
        'D3':{'zt':3,'xinhuan':28800,'kaishi':1625,'yunxin':2700,'norun':[99,100] ,'ykai':0}
      },
    4:{ #20-25度
        'D1':{'zt':4,'xinhuan':43200,'kaishi':257,'yunxin':15,'norun':[16,17,18,19,20,21,22],'ykai':1},
        'D2':{'zt':4,'xinhuan':2400,'kaishi':116,'yunxin':50,'norun':[16,17,18,19,20,21,22],'ykai':2},
        'D3':{'zt':4,'xinhuan':28800,'kaishi':1625,'yunxin':2700,'norun':[99,100] ,'ykai':0}
      },
    5:{ #25-30度
        'D1':{'zt':5,'xinhuan':28800,'kaishi':257,'yunxin':15,'norun':[16,17,18,19,20,21,22],'ykai':2},
        'D2':{'zt':5,'xinhuan':1800,'kaishi':116,'yunxin':60,'norun':[16,17,18,19,20,21,22],'ykai':2},
        'D3':{'zt':5,'xinhuan':28800,'kaishi':1625,'yunxin':2700,'norun':[99,100] ,'ykai':0}
      },
    6:{ #30-35度
        'D1':{'zt':6,'xinhuan':10800,'kaishi':257,'yunxin':12,'norun':[16,17,18,19,20,21,22],'ykai':3},
        'D2':{'zt':6,'xinhuan':1200,'kaishi':116,'yunxin':60,'norun':[16,17,18,19,20,21,22],'ykai':2},
        'D3':{'zt':6,'xinhuan':28800,'kaishi':1625,'yunxin':2700,'norun':[99,100] ,'ykai':0}
      },
    7:{ #35-40度
        'D1':{'zt':7,'xinhuan':3600,'kaishi':257,'yunxin':8,'norun':[16,17,18,19,20,21,22],'ykai':3},
        'D2':{'zt':7,'xinhuan':900,'kaishi':116,'yunxin':60,'norun':[16,17,18,19,20,21,22],'ykai':2},
        'D3':{'zt':7,'xinhuan':28800,'kaishi':1625,'yunxin':2700,'norun':[99,100] ,'ykai':0}
      },
    8:{ #40度以上
        'D1':{'zt':8,'xinhuan':1800,'kaishi':257,'yunxin':8,'norun':[16,17,18,19,20,21,22],'ykai':2},
        'D2':{'zt':8,'xinhuan':600,'kaishi':116,'yunxin':60,'norun':[16,17,18,19,20,21,22],'ykai':2},
        'D3':{'zt':8,'xinhuan':28800,'kaishi':1625,'yunxin':2700,'norun':[99,100] ,'ykai':0}
      },
   }
