import pynput
import time
import pydirectinput

# mouse = pynput.mouse.Controller()
#
#
b = int(input('点击次数：'))
c = float(input('间隔时间：'))

# d = int(input('1.开始 2.退出:'))
#
# def start():
#     print("请将鼠标移动到要连点的位置！")
#     for i in range(3):
#         print(r'距离程序运行还有%d秒！'%(3-i))
#         time.sleep(1)
#
# def click():
#     a = 1
#     while(a <= b):
#         mouse.press(pynput.mouse.Button.left)
#         mouse.release(pynput.mouse.Button.left)
#         a += 1
#         time.sleep(c)
#
# if __name__ == '__main__':
#     if d == 1:
#         start()
#         click()
#     if d == 2:
#         quit()


""""""""""""""""""""""""""""""



jianpan = pynput.keyboard.Controller()
a = 1

for i in range(3):
    print(r'距离程序运行还有%d秒！'%(3-i))
    time.sleep(1)

while(a <= b):
    pydirectinput.keyDown('a')
    pydirectinput.keyUp('a')
    time.sleep(c)
    pydirectinput.keyDown('d')
    pydirectinput.keyUp('d')
    a += 1
    time.sleep(c)
