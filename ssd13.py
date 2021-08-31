from machine import Pin,I2C
import ssd1306
import time
import network

class ssd:
  def __init__(self):
    self.lcd = ssd1306.SSD1306_I2C(128,64,I2C(scl=Pin(5), sda=Pin(4), freq=200000)) 
    self.myip = str(network.WLAN(network.STA_IF).ifconfig()[0])
    self.zt = str(2)
    self.temp = str(0)
    self.hum = str(50)
    
    
  def beginshow(self):
    self.lcd.fill(0)  #清空之前信息
    tim=time.localtime()
    if tim[3]< 16:
      mdata="D:" + str(tim[1]) + "-" + str(tim[2])
      mdata1=" " + str(tim[3]+8) +":" + str(tim[4])
    else:
      mdata="D:" + str(tim[1]) + "-" + str(tim[2]+1)
      mdata1=" " + str(tim[3]-16) +":" + str(tim[4])
    mytemp = "T: " + str(self.temp)
    myhum = "H: " + str(self.hum) 
    myzt = "ZT: " + str(self.zt)
    self.lcd.text(mytemp, 0, 0)
    self.lcd.text(myhum, 0, 16)
    self.lcd.text(mdata, 72, 0)
    self.lcd.text(mdata1, 74, 16)
    self.lcd.text(myzt, 0, 38)
    self.lcd.text(str(self.myip), 12, 56)
    for i in range(0, 28):
      self.lcd.pixel(2*i, 10, 1)
      self.lcd.pixel((2*i+74), 10 ,1)
    self.lcd.line(0, 12, 54, 12, 1)       #draw a line from (0,12) to (54,12) in blue
    self.lcd.line(74, 12, 128, 12, 1)

    self.lcd.hline(10, 32, 108, 1)        #draw a horizontal line,from (10,32),length 108 in blue
    self.lcd.vline(64, 0, 53, 1)          #draw a vertical line,from (64,0),length 64 in blue
    self.lcd.fill_rect(59, 27, 10, 10, 1) #draw a rectangle,from (59,27) to (10,10) fill with blue
    self.lcd.rect(56, 24, 16, 16, 1)      #draw a rectangle frame,from (59,27) to (10,10) in blue
    
    self.lcd.show() 