print("---리스트 함축---")
lst = list(range(1,11))
print([i**2 for i in lst if i >5])
fruits = ("apple", "orange", "kiwi")
print([len(i) for i in fruits])

