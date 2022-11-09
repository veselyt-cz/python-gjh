number = None

while True:
    try:
        number = int(input("Enter number: "))
        if number >= 1 and number <= 15:
            break
        else:
            print("Too low or high - try again!")
    except ValueError:
        print("Not a number - try again!")
