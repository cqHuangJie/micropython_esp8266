# Complete project details at https://RandomNerdTutorials.com

from machine import Pin#导入引脚类
from time import sleep#导入延时类

led = Pin(2, Pin.OUT)#实例化引脚为输出模式

while True:#无限循环
  led.value(not led.value())#引脚电平反置，控制小灯亮、灭
  sleep(0.5)#延时0.5秒
