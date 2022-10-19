total = 0

while True:
    entry = input()
    if entry == "":
        break
    number = int(entry)
    total += number

print("Sum: " + str(total))
