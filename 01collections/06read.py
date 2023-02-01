file = open("data/babicka.txt", encoding="utf-8")

data = file.read()

words = data.split(" ")
print(words[0])
print(len(words))

rows = data.split("\n")
print(len(rows))

file.close()
