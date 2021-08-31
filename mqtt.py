from umqtt.robust import MQTTClient
from machine import Pin, Timer, reset
import time
#import dht
import ujson as json
#import urequests as requests
import ssd13
import DHTsensor
#import kaiguanconfig as kai


class mqtt:

    def __init__(self, client_id='', username='', password='', server=""):
        self.server = server
        self.client_id = client_id
        self.username = username
        self.password = password
        #self.topic = (chipid() + '-sub').encode('ascii') if client_id == '' else (client_id + '-' + chipid() + '-sub').encode('ascii')

        self.topic = b"temp"
        self.mqttClient = MQTTClient(
            self.client_id, self.server, 6002, self.username, self.password)
        #self.dht11 = dht.DHT11(Pin(14))
        self.dht11 = DHTsensor.DHT12(Pin(14))
        self.pid = 0  # publish count
        self.failed_count = 0
        self.pub_count = 0
        self.ssd = ssd13.ssd()
        self.temp_count = 0
        self.tempcon = [1, 1, 0]

    def isPin(self, pin='-1'):
        if int(pin) in (0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16):
            return int(pin)
        else:
            return -1

    def pubData(self, t):
        self.dht11.measure()
        mytemp = self.dht11.temperature()
        myhumi = self.dht11.humidity()
        # 开始设计温控,每3分钟看下变化
        if self.temp_count == 4:
            self.tempcontrol(mytemp)
            self.temp_count = 0
        else:
            self.temp_count += 1
        # 配置显示属性
        self.ssd.temp = str(mytemp)
        self.ssd.hum = str(myhumi)
        # 开始组装要提交的数据
        value = {'datastreams': [{"id": "temp", "datapoints": [{"value": mytemp}]}, {
            "id": "humi", "datapoints": [{"value": myhumi}]}]}
        jdata = json.dumps(value)
        jlen = len(jdata)
        bdata = bytearray(jlen+3)
        bdata[0] = 1  # publish data in type of json
        bdata[1] = int(jlen / 256)  # data lenght
        bdata[2] = jlen % 256      # data lenght
        bdata[3:jlen+4] = jdata.encode('ascii')  # json data
        # 组装完毕
        try:
            print('show data:', str(self.pid + 1),
                  ' Temp:', mytemp, ' Humi:', myhumi)
            self.ssd.beginshow()  # 更新显示
            if self.pub_count == 7:
                print('publish to OneNet: Temp:', mytemp, ' Humi:', myhumi)
                self.mqttClient.publish('$dp', bdata)
                self.pub_count = 0
            self.pub_count += 1
            self.pid += 1
            self.failed_count = 0
        except:
            print('publish err!!')
            self.failed_count += 1
            if self.failed_count >= 5:
                self.mqttClient.disconnect()
                print('ESP reset!!')
                # tim.deinit()
                reset()

    def sub_callback(self, topic, msg):
        print((topic, msg))
        cmd = msg.decode('ascii').split(" ")
        if len(cmd) == 3:
            if cmd[0] == 'pin' and self.isPin(cmd[1]) >= 0:
                value = Pin(int(cmd[1])).value()
                if cmd[2] == 'on':
                    value = 1
                elif cmd[2] == 'off':
                    value = 0
                elif cmd[2] == 'toggle':
                    value = 0 if value == 1 else 1

                # , value=(1 if cmd[2] == 'on' else 0))
                pin = Pin(int(cmd[1]), Pin.OUT)
                pin.value(value)
            else:
                print('Pin number outof range.')
            if cmd[0] == 'din':
                import kaiguanconfig as kai
                if cmd[2] == 'c1off':
                    kai.c1.stop()
                elif cmd[2] == 'c2off':
                    kai.c2.stop()
                elif cmd[2] == 'c3off':
                    kai.c3.stop()
                elif cmd[2] == 'c1on':
                    kai.c1.begin()
                elif cmd[2] == 'c2on':
                    kai.c2.begin()
                elif cmd[2] == 'c3on':
                    kai.c3.begin()

    def connect(self):
        self.mqttClient.DEBUG = True
        self.mqttClient.set_callback(self.sub_callback)
        self.mqttClient.connect()
        print("Connected to %s, subscribed to %s topic." %
              (self.server, self.topic))
        tim = Timer(-1)
        # Timer.PERIODIC   Timer.ONE_SHOT
        tim.init(period=30000, mode=Timer.PERIODIC, callback=self.pubData)
        self.mqttClient.subscribe(self.topic)
        #print("Connected to %s, subscribed to %s topic." % (self.server, self.topic))
        try:
            while 1:
                # self.mqttClient.wait_msg()
                self.mqttClient.check_msg()
                #self.failed_count = 0
        except:
            print('subwait err!!')
            self.failed_count += 1
            if self.failed_count >= 5:
                print('ESP reset!!')
                self.mqttClient.disconnect()
                tim.deinit()
                reset()
        finally:
            # self.mqttClient.unsubscribe(self.topic)
            # self.mqttClient.disconnect()
            print('mqtt closed')
            # tim.deinit()
            # reset()

    def tempcontrol(self, temp):  # 温度控制函数
        import kaiguanconfig as kai
        self.ssd.zt=str(kai.c1.zt)  #传递显示状态
        if int(kai.c1.zt) != int(temp/5):
            if self.tempcon[2] == 3:
                self.tempcon[2] = 0

                # 开始调整
                for kon in [kai.c1, kai.c2, kai.c3]:
                    if kon.zhuangtai == True:
                        kon.stop()  # 停止前一个已经启动的定时程序
                time.sleep(1)
                print(kai.c1.xunhuan)
                kai.dinshi_config(temp)
                print(kai.c1.xunhuan)
                time.sleep(1)
                for kon in [kai.c1, kai.c2, kai.c3]:
                    if kon.zhuangtai == False:
                        kon.begin()

                # kai.dinshi_config(temp)
            else:
                self.tempcon[2] += 1  # 不一至计数器加1，连续3次后开始调整
        else:
            self.tempcon[2] = 0  # 其中任意有一次一至计数器均至零，避免误调整
    '''
    搞清楚了为什么重新设置后没有马上开始dinshi对象中的open操作了，是因为dinshi.count没有清零，继续执行着上次的计数
    反而有了延续性，因设计错误而得到好的结果，这样就不至于每次更新后又重新喷淋了。反而达到设计目的。最后决定还是加入
    stop 和 begin以避免同时读写 变量
    '''
