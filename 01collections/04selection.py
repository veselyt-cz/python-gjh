numbers = [50, 48, 26, 70, 86, 92, 90]

for j in range(0, len(numbers) - 1):
    m = j
    for i in range(j + 1, len(numbers)):
        if numbers[i] < numbers[m]:
            m = i
    t = numbers[m]
    numbers[m] = numbers[j]
    numbers[j] = t

print(numbers)
