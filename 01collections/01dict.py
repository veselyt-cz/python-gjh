letters = {"a": 2, "b": 4, "c": 6}

print(letters["a"])     # 2
print(len(letters))     # 3

letters["b"] += 4
print(letters["b"])     # 8

letters["d"] = 4
print(letters["d"])     # 4

letters.pop("a")
letters.pop("c")

print(letters)              # {'b': 8, 'd': 4}
print(letters.keys())       # ['b', 'd']
print(letters.values())     # [8, 4]
