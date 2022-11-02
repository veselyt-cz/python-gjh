total = 0
count = 0
minimum = None
maximum = None

while True:
    entry = input()
    if entry == "":
        break
    try:
        number = int(entry)
    except ValueError:
        continue
    total += number
    count += 1
    if minimum is None or number < minimum:
        minimum = number
    if maximum is None or number > maximum:
        maximum = number

print("Sum: " + str(total))
print("Count: " + str(count))
print("Minimum: " + str(minimum))
print("Maximum: " + str(maximum))
