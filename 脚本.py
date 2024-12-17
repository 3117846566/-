import pyautogui
import pygetwindow as gw
import time
import subprocess
def open_qibittottrent():
    qb_path = r"D:\qBittorrent\qbittorrent.exe"
    subprocess.Popen([qb_path])
def input_magent_link():
    #读取文件
    with open("file.txt",'r') as file:
        magents = [lines.strip() for lines in file.readlines()]


    windows = gw.getWindowsWithTitle("qBittorrent")

    if windows:
        qb_window = windows[0]
        qb_window.activate()
        time.sleep(3)

        pyautogui.hotkey('ctrl','shift','o')
        time.sleep(3)
        pyautogui.click(916,666)

        
        for mengent in magents:
            pyautogui.write(mengent)
            pyautogui.press('Enter')
        pyautogui.click(x=1194, y=891)

if __name__ == '__main__':
    open_qibittottrent()
    input_magent_link()

