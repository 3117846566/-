from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

# 创建Chrome浏览器对象，这里假设ChromeDriver已经配置好环境变量，如果没有配置好，可通过executable_path参数指定其具体路径，比如executable_path='C:/path/to/chromedriver.exe'（Windows下路径示例）


try:
    # 打开网页，这里以百度为例，你可以替换成你实际想打开的网址

     # 等待网页加载完成，可根据实际网络情况适当调整等待时间
    input_text = input("输入你想看的电影名:")
    time.sleep(10)
    # 通过定位元素找到输入框，这里以百度搜索框的id属性来定位（不同网页输入框定位方式不同，可能是通过name、class等属性，按需调整）
    driver = webdriver.Edge()
    driver.get("https://www.cilixiong.com/")
    search_input = driver.find_element(By.CLASS_NAME, "form-control.form-control-dark.text-bg-dark")
    # 输入你想要的文本内容，这里示例输入"Python自动化测试"，你可以替换成任意内容
    search_input.send_keys(input_text)
    search_input.send_keys(Keys.ENTER)
    movie = driver.find_element(By.CLASS_NAME,value="card-img")
    movie.click()
    url = driver.current_url
    number_pattern = re.compile(r"\d+")
    id = number_pattern.findall(url)[0]
    print(id)


finally:
    # # 操作完成后关闭浏览器
    time.sleep(3)
    driver.quit()
# <div class="card-img" style="background-image: url('https://i.nacloud.cc/2019/01195.webp');"><span></span></div>