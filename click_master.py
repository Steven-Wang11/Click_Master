import win32api
import win32con
import time
import keyboard
import pyautogui

def main(x, y, t): # 連點function(座標, 次數)
    for i in range(t):
        win32api.SetCursorPos((x,y)) # 滑鼠移到座標位置
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                            win32con.MOUSEEVENTF_LEFTUP,x,y,0,0) # 左鍵點
        print('連點了 %d 次'%(i + 1), end = '\r')
        if keyboard.is_pressed('esc'): # 中途能按esc中斷
            break
        time.sleep(0.05) # 連點時間間隔毫秒


def cordinate():
    print('請滑到你要連點的位置後，按下Esc開啟')
    while True:
        cord = pyautogui.position()
        print(cord, end = '\r')
        time.sleep(0.05)
        if keyboard.is_pressed('esc'):
            break
    return cord


if __name__  == '__main__':
    con = 0
    cord = cordinate()
    x = cord[0] # x座標
    y = cord[1] # y座標
    while True:
        t = int(input('\n幾次 = '))
        print('中途可按 Esc 中斷')
        main(x, y, t)
        print('\n是否繼續，確定請按"e"否"esc"：')
        k = keyboard.read_key()
        if k == 'e':
            pass
        else:
            break
    exit()
