#web1.py
#웹크롤링
from bs4 import BeautifulSoup

#페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색에 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#전체 보기
#print(soup.prettify())
#<p>태그 전체를 검색
# print(soup.find_all("p"))
#첫번째 <p>만 검색
#print(soup.find("p"))
#<p class="outer-text">형태만 검색
#print(soup.find_all("p", class_="outer-text"))  #파이썬에는 class가 키워드야. 충돌이 일어나서 언더바를 붙인다.
#attrs를 사용(Attributes)
#print(soup.find_all("p", attrs_={"class":"outer-text"}))
#특정 태그만 지정할 경우 id속성
# print(soup.find_all(id="first"))
#태그 내부의 컨텐츠를 가져오기: .text
for tag in soup.find_all("p"):
    title = tag.text.strip()
    print(title)
    

