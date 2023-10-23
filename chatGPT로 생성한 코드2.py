# 리스트 (List)
my_list = [1, 2, 3, 4, 5]  # 가변적(mutable), 인덱스로 접근 가능, 순서가 있음
list_example = []
list_example.append(1)  # 요소 추가
list_example.remove(1)  # 요소 삭제
print("List Example:", list_example)

# 튜플 (Tuple)
my_tuple = (1, 2, 3, 4, 5)  # 불변적(immutable), 인덱스로 접근 가능, 순서가 있음
tuple_example = (1, 2)
print("Tuple Example:", tuple_example)

# 세트 (Set)
my_set = {1, 2, 3, 4, 5}  # 가변적(mutable), 중복된 요소를 허용하지 않음, 순서가 없음
set_example = {1, 2}
set_example.add(3)  # 요소 추가
set_example.remove(2)  # 요소 삭제
print("Set Example:", set_example)

# 딕셔너리 (Dictionary)
my_dict = {'a': 1, 'b': 2, 'c': 3}  # 가변적(mutable), 키-값 쌍으로 이루어짐, 순서가 없음
dict_example = {'a': 1, 'b': 2}
dict_example['c'] = 3  # 요소 추가/수정
del dict_example['a']  # 요소 삭제
print("Dictionary Example:", dict_example)