from machine import Pin, Timer
import time

class dinshi:
    def __init__(self):
        self.xunhuan="100"
        self.kaishi="10"
        self.yunxin="2"
        self.port=12
        self.conut=0
        self.biaoji=0
        self.biaoji2=0
        self.norun=[99,100]
        self.ykai=0
        self.ykaiconut=0
        self.zhuangtai= False
        self.zt = 1
        self.zt2='new'
    
    def begin(self):
      self.jieshu = int(self.kaishi + self.yunxin)
      self.pin = Pin(int(self.port), Pin.OUT)
      self.tim = Timer(-1)
      self.tim.init(period=1000, mode=Timer.PERIODIC, callback=self.my_callback)
      self.zhuangtai = True
      print('dinshi on %s is begin!' %str(self.zt2))
      
    def stop(self):
      self.tim.deinit()
      self.zhuangtai = False
      print('dinshi on %s is stop!' %str(self.zt2))  
      
    def my_callback(self,t):
      self.conut+=1
      if self.kaishi >= self.conut:
        pass
        #print("<<<<<kaishi" +str(self.port))
      if self.kaishi < self.conut <= self.jieshu:
        if self.biaoji == 0:
          thtime = time.localtime()[3] #注意此处，可能因未锁出错
          if thtime in self.norun:  #夜间模式判读
            if self.ykai == 0:
              pass
            else:
              self.ykaiconut +=1
              if self.ykaiconut == self.ykai: 
                self.pin.on()
                print("----------yejian_open_"+str(self.port)+"----------")
                self.ykaiconut = 0  #夜间模式计数归零
          else:  
            self.pin.on()
            print("----------open_"+str(self.zt2)+"----------")
        self.biaoji = 1   
      if self.conut > self.jieshu:
        if self.biaoji2 == 0:
          self.pin.off()
          print("----------close_"+str(self.zt2)+"----------")
        self.biaoji2 = 1
      if self.conut > self.xunhuan:  #循环参数归零
        self.conut = 0
        self.biaoji = 0
        self.biaoji2 = 0
      #if self.ykaiconut >= self.ykai:  #夜间模式参数归零
      #  self.ykaiconut = 0  