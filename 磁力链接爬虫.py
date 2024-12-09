import requests
import re
from bs4 import BeautifulSoup
# def find_id():
#     id
#     return id
def request_funcation(id,kind):
    headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    url = "https://www.cilixiong.com/movie/4175.html"
    request = requests.request(method='GET', url=url, headers=headers)
    request.encoding = "UTF-8"
    source = request.text


soup = BeautifulSoup(source,'html.parser')
# for i in soup.find_all('a'):
#     print(i)
# class_="d-flex align-items-center mb-2 mb-lg-0 px-5 logo"
a_tags = soup.find_all('a')

magent_pattern = re.compile(r'magnet:\?.*')
try:
    with open('file.txt','w') as file:
        for a_tag in a_tags:
            href = a_tag.get('href')
            if href and magent_pattern.match(href):
                print(href)
                file.write(href+'\n')
except Exception:
    print("error")






