import pynput
import time
import pydirectinput

num = int(input("输入循环的次数:"))

_mouse = pynput.mouse.Controller()

star = 1

_time = float(input("请输入每次挖掘时间："))

time_ = float(input("每次行走的时间:"))

for i in range(5):
    print(r'距离程序运行还有%d秒！'%(5-i))
    time.sleep(1)

while star <= num:
    _mouse.press(pynput.mouse.Button.left)
    time.sleep(_time)
    _mouse.release(pynput.mouse.Button.left)
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown('w')
    time.sleep(time_)
    pydirectinput.keyUp('w')
    pydirectinput.keyUp('shift')
    
    star += 1






