file = open("data/babicka.txt", encoding="utf-8")

words = {}

data = file.read()
for word in data.split(" "):
    if word not in words:
        words[word] = 0
    words[word] += 1

maximum = None
for word in words:
    count = words[word]
    if maximum is None or count > words[maximum]:
        maximum = word

print(maximum + " " + str(words[maximum]))
