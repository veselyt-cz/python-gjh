numbers = [3, 5, 7, 9, 11]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

for number in numbers:
    print(number)

i = 0
while i < len(numbers):
    print("Number " + str(i + 1) + " is " + str(numbers[i]))
    i += 1

for i in range(0, len(numbers)):    # [0, 1, 2, 3, 4]
    print("Number " + str(i + 1) + " is " + str(numbers[i]))
