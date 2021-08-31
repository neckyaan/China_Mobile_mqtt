import dinshi
from data import Dinshi_data as data
#常温定时对象
c1=dinshi.dinshi()
c2=dinshi.dinshi()
c3=dinshi.dinshi()
def dinshi_config(mytemp):
    temp = 1
    try:
        if int(mytemp) <5:
            temp = 0
        elif 5 <= int(mytemp) <40:
            temp = int(mytemp / 5)
        elif 40 <= int(mytemp):
            temp =8    
        print("temp_set_ok is %s" %str(temp))

    except:
        print("temp_set_err is %s" %str(mytemp))
        temp = 1    
    try:
    #第一路
        global c1,c2,c3
        c1.xunhuan=data[temp]['D1']['xinhuan']
        c1.kaishi=data[temp]['D1']['kaishi']
        c1.yunxin=data[temp]['D1']['yunxin']
        c1.norun=data[temp]['D1']['norun']
        c1.ykai=data[temp]['D1']['ykai']
        c1.zt=data[temp]['D1']['zt']
        c1.zt2="D1_port_12" + "_temp_"+ str(temp)
        c1.port=12
        #第二路
        c2.xunhuan=data[temp]['D2']['xinhuan']
        c2.kaishi=data[temp]['D2']['kaishi']
        c2.yunxin=data[temp]['D2']['yunxin']
        c2.norun=data[temp]['D2']['norun']
        c2.ykai=data[temp]['D2']['ykai']
        c2.zt=data[temp]['D2']['zt']
        c2.zt2="D2_port_13" + "_temp_"+ str(temp)
        c2.port=13
        #第三路
        c3.xunhuan=data[temp]['D3']['xinhuan']
        c3.kaishi=data[temp]['D3']['kaishi']
        c3.yunxin=data[temp]['D3']['yunxin']
        c3.norun=data[temp]['D3']['norun']
        c3.ykai=data[temp]['D3']['ykai']
        c3.zt=data[temp]['D3']['zt']
        c3.zt2="D3_port_15" + "_temp_"+ str(temp)
        c3.port=15
        print('temp_config is %s' %str(temp))
    except:
        print("temp_config is err on %s" %str(mytemp))   