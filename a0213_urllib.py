import urllib.request
url = 'http://uta.pw/shodou/img/28/214.png'
savename = 'test12.png'

urllib.request.urlretrieve(url, savename)

# 다운로드
import urllib.request
url = 'http://uta.pw/shodou/img/28/214.png'
savename = 'test21.png'

mem = urllib.request.urlopen(url).read()

with open(savename, mode='wb') as f:
    f.write(mem)
    print("저장되었습니다")

#추가
import urllib.request
url = "http://www.google.co.kr/"

mem1 = urllib.request.urlopen(url).read()
print(mem1.decode("euc-kr"))

# API로 접근해서 결과 출력하기
import urllib.request

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)

#요청 방식(get, post, put, delete)
#요청 대상(http://daum.net)
#추가적인 정보
 # 경로 : /photo-viewer/3489534795
 # 데이터 : ?cid=318190

#네이버창에 초콜릿이라고 검색하면 ?

#https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF
#방식 : GET
#대상 : https://search.naver.com => 호스트 이름
#추가적인 정보
 # 경로 : /search.naver
 # 데이터 : ?sm=top_hty
# &fbm=1
# &ie=utf8
# &query=초콜릿 <=오른쪽껄 디코딩  %EC%B4%88%EC%BD%9C%EB%A6%BF <= 초콜릿에 대응되는 인코딩된 문자

import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"
values = {
    "sm": "top_hty",
    "fbm": "1",
    "ie":"utf8",
    "query":"초콜릿"
}
params = urllib.parse.urlencode(values)

#어떻게 나오는지 보자
print(api)
print(params)

url = api+"?"+params
print(url)

data = urllib.request.urlopen(url).read()
print(data)
#b'<!doctype html> <html lang="ko"> <head> <meta charset="ut
#결과 이렇게 나오는데 b로 시작해서 바이너리파일
text = data.decode("utf-8") #euc-kr이란 방법도 있다
print(text)
