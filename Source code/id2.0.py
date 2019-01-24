import requests
import os
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")

def getText(html):
    new_html = (html.replace('<br>', '')).replace('<br/>', '')
    soup = BeautifulSoup(new_html, 'html.parser')
    text = soup.find_all('td', 'tdc2')
    return text[2].string

url = "http://qq.ip138.com/idsearch/index.asp?action=idcard&userid="
file_read = open("id.txt", "r")
i = 1
while True:
    url1 = file_read.readline()  # 读取file_read中的一行内容
    if not url1:
        break
    # url1 = input("输入身份证号：")
    url1 = url1.strip('\n')
    print(url+url1)
    html = getHTMLText(url + url1)
    dizhi = getText(html)
    print(dizhi)
    file = open("信息.txt", "a")
    file.write(dizhi + '\n')
    file.close()
    print("%d" % i)
    i = i + 1
file_read.close()
