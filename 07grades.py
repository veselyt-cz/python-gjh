count = 0
while not count > 0:
    try:
        count = int(input("Kolik mas znamek? "))
    except ValueError:
        print("To neni platne cislo!")

grades = 0
weights = 0

index = 1
while index <= count:
    grade = 0
    while not 1 <= grade <= 5:
        try:
            grade = int(input("Zadej " + str(index) + ". znamku: "))
        except ValueError:
            print("To neni platna znamka!")
    weight = 0
    while not 1 <= weight <= 3:
        try:
            weight = int(input("Zadej vahu " + str(index) + ". znamky: "))
        except ValueError:
            print("To neni platna vaha!")
    grades += grade * weight
    weights += weight
    index += 1

print("Vazeny prumer: " + str(round(grades / weights, 2)))
print("Znamka na vysvedceni: " + str(round(grades / weights)))
