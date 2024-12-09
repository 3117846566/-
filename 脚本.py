import pyautogui
import time
import tkinter as tk
from tkinter import filedialog

def read_file_content():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()  # 弹出文件选择对话框，让用户选择文件
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("文件未找到，请检查路径是否正确")
            return None
    else:
        print("未选择任何文件")
        return None

def add_to_qbittorrent(content):
    # 先确保qBittorrent客户端已经打开，如果没有打开需要手动打开或者通过代码来启动（比如通过subprocess模块调用启动命令，不同系统启动命令不同，这里暂不展开）
    # 模拟点击qBittorrent添加任务按钮（这里假设是Windows系统下，且qBittorrent界面是默认布局等情况，需要根据实际情况调整坐标等）
    pyautogui.click(x=100, y=200)  # 此处坐标需替换成qBittorrent中添加任务按钮实际所在坐标，可以通过截图工具查看坐标
    time.sleep(1)
    # 模拟粘贴操作（假设前面已经复制了文件内容或者直接输入内容到弹出的添加任务对话框中）
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # 模拟点击确定/开始下载等按钮（同样需根据实际界面布局确定坐标）
    pyautogui.click(x=300, y=400)  # 替换成实际对应按钮坐标
    time.sleep(1)

if __name__ == "__main__":
    file_content = read_file_content()
    if file_content:
        add_to_qbittorrent(file_content)

