#필터링하는 함수
lst = [10, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("---필터링하는 경우---")
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

#람다함수 적용
print("---람다함수---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)

#분기구문
  Ctrl + / 주석으로 변경됨
score = int(input("점수를 입력: "))
if 90 <= score <= 100:
    grade = "A"
if 80 <= score:
    grade = "B"
if 70 <= score:
    grade = "C"    
else:
    grade = "D"

print("등급은: ", grade)

#반복문
value = 5
while value > 0:
    print(value)
    value = 1

lst = ["apple", 100, 3.14]
for item in lst:
    print(lst, type(lst))

fruit = {"apple":100, "kiwi":200}
for item in fruit.items():
    print(item)

#수열함수
lst = lst(range(1,11))
print = lst
print("---break구문---")
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue구문---")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format)





