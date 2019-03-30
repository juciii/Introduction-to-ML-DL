# 뷰티풀수프

from bs4 import BeautifulSoup

html = """
<html><body>
    <div id="meigen">
     <h1>위키북스 도서</h1>
     <ul class="items">
      <li>유니티 게임 이펙트 입문</li>
      <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
      <li>모던 웹사이트 디자인의 정석</li>
     </ul>
    </div>
    </body>
</html>
"""

#태그 선택자
#"ul" #ul 태그를 선택하고자하면
#"div" #div 태그를 선택하고자하면 #은 이중에 이름을 선택
#class를 선택하고자 할때는 . 사용 즉, .items
#<ul class="items art it book"> 이렇게 되어 있으면 .book or .art or .it 등등
#ul.book.items.art 이렇게면 세개 다 입력된다.
#정리하자면,
 # 태그선택자
#  "h1"
#  "html"
 # 아이디선택자
#  "#<아이디 이름>"
 # 클래스 선택자
#  ".<클래스 이름>.<클래스 이름>"
 # 후손 선택자 띄어쓰기로
#  "html li"
#  "#meigen li"
 # 자식 선택자 > 표시로
#  "ul.items > li"

soup = BeautifulSoup(html, 'html.parser')
#soup.select_one("div#meigen")
list_items = soup.select("ul.items > li") #요소의 배열
header = soup.select_one("body > div > h1") # 요소

#header.string #글자 추출
#header.attrs #내부의 속성 추출
#header.attrs["title"] #내부의 title이라는 속성 추출

print(header.string)
print(soup.select_one("ul").attrs)
for li in list_items:
    print(li.string)

#네이버 금융에서 환율정보 추출하기

import urllib.request
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
soup.select_one()
results = soup.select("span.value")
for result in results:
    print(result.string)

# 네이버 뉴스 가져오기

# 네이버 뉴스 가져오기
import urllib. request
from bs4 import BeautifulSoup

url1 = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
response1 = urllib.request.urlopen(url1)

soup1 = BeautifulSoup(response1, "html.parser")
results1 = soup1.select("div.cluster_text a")
for result1 in results1:
    print(result1.string)
    print("링크:", result1.attrs["href"])
    print("")

# 기사 목록을 가져옵니다.
import urllib.request
from bs4 import BeautifulSoup
import time #서버에 부담을 덜기위해

url2 = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
response2 = urllib.request.urlopen(url2)
soup2 = BeautifulSoup(response2, "html.parser")
results2 = soup2.select("div.cluster_text a")
for result2 in results2:
    # 기사를 가져옵니다.
    print(result2.string)
    url_article = result2.attrs["href"]
    response22 = urllib.request.urlopen(url_article)
    soup22 = BeautifulSoup(response22, "html.parser")
    content22 = soup22.select_one("#articleBodyContents")
    # print(content22.contents)
    # 가공합니다.
    output = ""
    for item in content22.contents:
        stripped = str(item).strip()
        if stripped == "":
            continue
        if stripped[0] not in ["<","/"]:
            output += str(item).strip()
    print(output.replace("본문 내용TV플레이어", ""))
    time.sleep(30)  #30초 휴식


# 20 페이지 find 함수

import urllib.request
from bs4 import BeautifulSoup

html = """
<html><body>
 <h1 id="title">스크레이핑이란?</h1>
 <p id="body">웹 페이지를 분석하는 것</p>
 <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")

title = soup.find(id= "title").string
body = soup.find(id= "body")

print("#title=", title)
print("#body=", body.string)        #string 위치 봐바바


# 21 페이지 find_all() 매서드
import urllib.request
from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")
for link in links:
    href = link.attrs["href"]
    text = link.string
    print(text, ">", href)

# DOM 요소의 속성에 대해
from bs4 import BeautifulSoup
soup = BeautifulSoup(
    "<p><a href='a.html'>test</a></p>",
    "html.parser"
)
# 분석 제대로 됐는지 확인하기
print(soup.prettify())
# <a> 태그를 a에 할당
a = soup.p.a
# attrs 속성의 자료형 확인
print(type(a.attrs))
# href 속성이 있는지 확인
print('href' in a.attrs)
# href 속성값 확인
print(a['href'])

# urlopen()과 BeautifulSoup 조합하기
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

title = soup.find("title")
wf = soup.find("wf")
print(title.string)
print(wf.string)

#

# attrs 속성의 자료형 확인
print(type(a.attrs))


