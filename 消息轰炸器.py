from pynput.keyboard import Key
from pynput.keyboard import Controller
import time

keyboard = Controller()

a = input("请输入你要循环的内容：")
b = int(input("请你输入循环次数："))
c = float(input("请输入每次循环的间隔时间："))
print('ok!请将光标移动到会话框中')
time.sleep(2)

for i in range(3):
    print(r'距离程序运行还有%d秒！'%(3-i))
    time.sleep(1)

for i in range(b):
    keyboard.type(a)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(c)

print("消息发送完成")
