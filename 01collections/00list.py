numbers = [1, 3, 5, 7, 9]
names = ["Tobias", "Dan", "Timon"]

print(numbers[0])       # 1
print(numbers[1])       # 3
print(numbers[-1])      # 9

print(len(numbers))     # 5

names[0] = "David"
print(names[0])     # David

names.append("Filip")
print(names[3])     # Filip

names.remove("Dan")

print(names)    # ['David', 'Timon', 'Filip']

names.pop()
names.pop(0)

print(names)    # ['Timon']
