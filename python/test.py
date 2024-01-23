import urllib.request as req
from bs4 import BeautifulSoup
html = '<div class="title"><a>标题</a><span>其他内容</span></div>'
root = BeautifulSoup(html, "html.parser")

title = root.find("div", class_="title").a.string
print(title)  