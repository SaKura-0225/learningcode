import urllib.request as req
from bs4 import BeautifulSoup

def getdata(url):
    #用request.Request来构造带有headers的请求来伪造正常访问,headers(键值对)要用花括号包住
    request=req.Request(url,headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": "_gid=GA1.2.280063933.1705989865; _gat=1; over18=1; _ga_DZ6Y3BY9GW=GS1.1.1705995224.2.1.1705995244.0.0.0; _ga=GA1.1.763940139.1705989864"
        })
    with req.urlopen(request) as response:
        #使用 read() 函数获取网页的 HTML 实体代码。
        #read() 是读取整个网页内容,通过decode.()实现以utf-8解码
        data=response.read().decode("utf-8") 

    #创建一个BeautifulSoup解析对象
    root=BeautifulSoup(data,"html.parser")

    #(寻找带有class=“title”属性的div标签)
    #获取到一个<div class="title"></div>标签组的列表
    #find_all 返回的是一个列表，而不是单个元素。在你的 HTML 结构中，每个标题都包含在一个 div 元素内，而 find_all 会返回匹配条件的所有元素的列表
    #所以这样写是不对的（root.find_all("div",class_="title").a.text）
    #因此，如果想要获取所有标题的文本内容，需要遍历这个列表，并对每个元素使用 .a.text 获取文本。

    titles=root.find_all("div",class_="title")

    #获取第一个标题的内容
    first_title = root.find_all("div", class_="title")[0].a.string
    print(first_title)

    #获取所有标题的内容
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextlink=root.find("a",string="‹ 上頁")
    return nextlink["href"]


url="https://www.ptt.cc/bbs/movie/index.html"

count=0
while count<3:
    url="https://www.ptt.cc"+getdata(url)
    count+=1