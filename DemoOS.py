# DemoOS.py
from os.path import *
from os import *
import glob

print("전체경로:", abspath("python.exe"))
print("파일명:", basename("c:\\work\\demo.txt"))

stryPython = "c:\\python210\\python.exe"
if exists(stryPython):
    print("파일크기:{0}".format(getsize(stryPython)))

else:
    print("파일없음")

# #외부 실행파일
# system("notepad.exe")

# #운영체제
print("운영체제이름:", name)
print("환경변후:", environ)

# result = glob.glob("c:\\work\\*.py")
# print(result)
for item in glob.glob("c:\\work\\*."):
    print(item)

