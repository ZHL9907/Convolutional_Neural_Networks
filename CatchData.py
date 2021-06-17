import re
import time
#from docx import Document
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
list1=[]

HuaType="茉莉花"

for j in range(1,7):
    url ='https://www.ivsky.com/search.php?q=%E8%8C%89%E8%8E%89%E8%8A%B1&page='+ str(j)
    print(url)
    resp = requests.get(url,headers=headers)
    resp.encoding = 'utf-8'

    # 把源代码交给page
    main_page = BeautifulSoup(resp.text, "html.parser")
    # 找到class为TypeList 中属性为a的源代码
    alist = main_page.find("div", class_="left").find_all("img")
    obj = re.compile(r'[a-zA-z]+://[^\s]*',re.S)
    a = obj.finditer(str(alist))

    #数据清洗并存储（图片下载网址）
    # list1.clear()
    for i in a:
        img_name = i.group()
        img_name2 = img_name.split('\"')[0]
        list1.append(img_name2)

    # for i in range (len(list1)):
    #        print(list1[i])

    #保存picture
    for i in range(len(list1)):
        picture=requests.get(list1[i],headers=headers)
        filename = './训练集/'+HuaType+'/'+HuaType + str(i) + '.jpg'
        with open(filename,mode='wb')as f:
            f.write(picture.content)

