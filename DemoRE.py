#DemoRe.py
#정규표현식(특정한 규칙)
import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())
# #함정 추가
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")  #apple을 찾아줘
print(result.group())

result = re.search("\d{4}", "올해는 2023년입니다.")  #4자리 숫자를 찾아줘
print(result.group())

result = re.search("\d{5}", "우리 동네는 52300")  #숫자가 연속으로 5자리 숫자를 찾아줘
print(result.group())

#컴파일 함수를 사용
data = "Apple is big company and apple is delicious"
c = re.compile("apple", re.IGNORECASE)
print(c.findall(data))

data = """다중 라인으로
만든 문자열

데이터"""

c = re.compile("^.+", re.MULTILINE)
print(c.findall(data))

