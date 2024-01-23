#实现拉取台北某地瓦斯行名稱和其对应地址与电话号码并做整理
#用class对重复工作进行封装

import urllib.request as req
import json
import ssl

class LIST:      #创建类“LIST”
    def __init__(self,listname):     #定义初始化函数，获取需要建立的列表名称“listname”，预先定义抓取的最初列表变量为“init_list”且暂时为空
        self.listname=listname
        self.init_list=None
    def requrl(self,url):       #定义爬虫方法，获取需要抓取的api的网站‘url’,完成对数据的初步提取并将内容制作成init_list列表
        ssl._create_default_https_context = ssl._create_unverified_context
        with req.urlopen(url) as response:
            self.init_list=json.load(response)["result"]["results"]
    def make(self,element):      #定义对所需内容进行分组的方法，将不同类别内容“element”制作成相应的列表
        self.listname=[]
        for i in self.init_list:
           a=i[element]
           self.listname.append(a)

#分别创建三个实体“L1,L2,L3”，制作相应的三个列表
L1=LIST("namelist")
L1.requrl("https://data.taipei/api/v1/dataset/9bfad0fe-848a-4bb5-b2e3-c57d5dc50bdb?scope=resourceAquire")
L1.make("瓦斯行名稱")

L2=LIST("tellist")
L2.requrl("https://data.taipei/api/v1/dataset/9bfad0fe-848a-4bb5-b2e3-c57d5dc50bdb?scope=resourceAquire")
L2.make("電話")

L3=LIST("addlist")
L3.requrl("https://data.taipei/api/v1/dataset/9bfad0fe-848a-4bb5-b2e3-c57d5dc50bdb?scope=resourceAquire")
L3.make("營業地址")

#对列表内容进行整合
i=0
data=[]
while i<len(L1.listname):
    data.append("公司名称: "+L1.listname[i]+" 公司地址: "+L3.listname[i]+" 公司电话: "+L2.listname[i])
    i+=1

#将信息写入到文件中完成信息整理
with open("information(class).txt", "w", encoding="utf-8") as file:
    for x in data:
        file.write(x+"\n")