import win32gui
from PIL import ImageGrab
import win32con
import time
from pynput.mouse import Button, Controller
import aotopy
mouse = Controller()

__hwnd = win32gui.FindWindow(0,"梦幻西游 ONLINE - (江苏3区[春风十里] - ㄧ赖Ⅵ雪慈[42022437])")
if not __hwnd:
    print('window not found!')
    exit()
win32gui.SetForegroundWindow(__hwnd)
win32gui.ShowWindow(__hwnd, win32con.SW_RESTORE)  
gamerect = win32gui.GetWindowRect(__hwnd)  #(left, top, right, bottom) 
hcenter = int((gamerect[2] - gamerect[0])/2)+gamerect[0]
vcenter = int((gamerect[3] - gamerect[1])/2)+gamerect[1]
time.sleep(10)
mouse.position = (hcenter, vcenter)  #initialize mouse position
print(gamerect)
print(hcenter,' ',vcenter)


# from pynput import mouse

# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))

# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     if not pressed:
#         # Stop listener
#         return False

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))

# # Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()