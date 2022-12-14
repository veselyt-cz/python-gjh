file = open("14advent.txt")
lines = file.read().splitlines()

total = 0
maximum = 0

for line in lines:
    if line == "":
        if total > maximum:
            maximum = total
        total = 0
    else:
        total += int(line)

print(total)
