# List (리스트) - 가변 (mutable)
my_list = [1, 2, 3, 4, 5]

# Tuple (튜플) - 불변 (immutable)
my_tuple = (1, 2, 3, 4, 5)

# Set (집합) - 중복 요소가 없고 순서가 없음
my_set = {1, 2, 3, 4, 5}

# Dictionary (사전) - 키-값 쌍으로 구성
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# List (리스트)의 장단점
list_advantages = "가변, 색인을 사용한 원소 접근 가능, 순서가 유지됨"
list_disadvantages = "요소 검색 시 느릴 수 있음, 중복 요소 허용"

# Tuple (튜플)의 장단점
tuple_advantages = "불변, 빠른 요소 접근, 해시 가능 (딕셔너리의 키로 사용 가능)"
tuple_disadvantages = "요소 변경 불가, 요소 추가 불가"

# Set (집합)의 장단점
set_advantages = "중복 요소 제거, 빠른 집합 연산 (교집합, 합집합 등)"
set_disadvantages = "순서가 없음, 색인을 사용한 요소 접근 불가"

# Dictionary (사전)의 장단점
dict_advantages = "키-값 쌍으로 데이터 구조화, 빠른 키를 사용한 검색"
dict_disadvantages = "키는 유일해야하며 불변, 순서가 없음"

# 결과 출력
print("List (리스트):")
print("장점:", list_advantages)
print("단점:", list_disadvantages)

print("\nTuple (튜플):")
print("장점:", tuple_advantages)
print("단점:", tuple_disadvantages)

print("\nSet (집합):")
print("장점:", set_advantages)
print("단점:", set_disadvantages)

print("\nDictionary (사전):")
print("장점:", dict_advantages)
print("단점:", dict_disadvantages)