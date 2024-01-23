#实现拉取台北某地瓦斯行名稱和其对应地址与电话号码并做整理

import urllib.request as req
import json
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

#urlopen( ) 方法
#用于打开一个远程的url连接,并且向这个连接发出请求,获取响应结果。返回的结果是一个http响应对象,这个响应对象中记录了本次http访问的响应头和响应体
#urllib.request.urlopen 参数介绍：
#urllib.request.urlopen(  url,   data=None,   [timeout, ]*,  cafile=None, capath=None, cadefault=False, context=None)



with req.urlopen("https://data.taipei/api/v1/dataset/9bfad0fe-848a-4bb5-b2e3-c57d5dc50bdb?scope=resourceAquire") as response:
    data=json.load(response)
init_list=data["result"]["results"]   #获取到一个列表，列表里面的元素是字典


#分别制作三个列表来存放名字，地址和电话
addlist=[]
tellist=[]
namelist=[]
for name in init_list:
    a=name["瓦斯行名稱"]   
    namelist.append(a)
for tel in init_list:
    b=tel["電話"]
    tellist.append(b)
for add in init_list:
    c=add["營業地址"]
    addlist.append(c)

#分别将名称地址与电话一一对应整合    
i=0
data=[]
while i<len(addlist):
    data.append("公司名称: "+namelist[i]+" 公司地址: "+addlist[i]+" 公司电话: "+tellist[i])
    i+=1

#将信息写入到文件中完成信息整理
with open("information.txt", "w", encoding="utf-8") as file:
    for x in data:
        file.write(x+"\n")