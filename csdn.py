#coding = utf-8
import requests
from bs4 import BeautifulSoup as bs
import re
import time

# 访问我的博客
def spider(url, headers):
    r = requests.get(url=url, headers=headers)
    html = r.text
    # 解析html代码
    soup = bs(html, 'lxml')
    ul = soup.find(name='ul', attrs={'id': 'blog_rank'})
    # 获取ul下的第一个li节点,正则表达式需要字符串，所以转化一下
    li = str(ul.find_next('li'))
    numbers = re.findall(r'span>(.+?)次</', li)
    # print(numbers)
    # 获取当前年月日
    date = time.strftime("%Y-%m-%d", time.localtime())
    # 拼接日期
    numbers.append(date)
    text_save(numbers, 'visitorNumber.txt')
    print('成功执行!')

# 文件存储
def text_save(content, filename, mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        # 如果索引为最后一位，去掉空格且拼上换行符，否则剩下的后面拼接逗号
        if i == len(content) - 1:
            number = (content[i]) + '\n'
        else:
            number = str(content[i]) + ','
        file.write(number)
    file.close()


if __name__ == '__main__':
	
    url = "http://blog.csdn.net/s740556472/article"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'blog.csdn.net',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    spider(url, headers)
