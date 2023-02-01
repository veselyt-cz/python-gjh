file = open("data/babicka.txt", encoding="utf-8")

letters = {}

data = file.read()
for letter in data:
    if letter not in letters:
        letters[letter] = 0
    letters[letter] += 1

maximum = None
for letter in letters:
    count = letters[letter]
    if maximum is None or count > letters[maximum]:
        maximum = letter

print(maximum + " " + str(letters[maximum]))
