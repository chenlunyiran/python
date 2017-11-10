# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

names = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(names["Bob"])
print("Bob" in names)
print("Jack" in names)
print(names.get("Bob"))
print(names.get("Jack"))
print(names.get("Jack","Jack"))     # dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(names.pop("Bob"))     # 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
names.setdefault("Jack",65)     # 添加一个key，value
for x in names:
    print(x)