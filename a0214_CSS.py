from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

a_list = soup.select("#mw-content-text > div > ul:nth-child(6) > li > b > a")
for alist in a_list:
    name = alist.string
    print("-", name)

# 추가적으로 다른 작품들
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

yoon_list = soup.select("#mw-content-text > div > ul:nth-child(6) > li a")
for yoon in yoon_list:
    name = yoon.string
    if name == "증보판":
        continue
    print("-", name)
    # (증보판 생략하기)

# books.html을 scripts 폴더에 넣어서 !!
from bs4 import BeautifulSoup

fp = open("books.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q : print(soup.select_one(q).string)
sel("#nu")
sel("li#nu")
sel("ul > li#nu")
sel("#bible > #nu")
sel("#bible > li#nu")
sel("li[id='nu']")

print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)


# 실행 왜 안돼지
from bs4 import BeautifulSoup

fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

#soup.select로 추출하기
print(soup.select_one("li:nth-of-type(8)").string)
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li#black")[1].string)

#find 매서드로 추출하기
cond = {
    "data-lo" : "us",
    "class" : "black"
}
print(soup.find("li", cond).string)


#find 매서드 연속으로 사용하기
print(soup.find(id="ve-list").find("li", cond).string)



# 40 페이지
from bs4 import BeautifulSoup
import re

html = """
<ul>
    <li><a href="hoge.html">hoge</li>
    <li><a href="https://example.com/fuga">fuga*</li>
    <li><a href="https://example.com/foo">foo*</li>
    <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
li = soup.find_all(href=re.compile(r"^https://"))
for e in li:
    print(e.attrs['href'])



