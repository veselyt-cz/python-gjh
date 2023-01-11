names = []
heights = []

while True:
    command = input("> ")
    if command == "a":
        name = input("name: ")
        height = int(input("height: "))
        if height > 0:
            names.append(name)
            heights.append(height)
    if command == "d":
        name = input("name: ")
        try:
            names.remove(name)
        except ValueError:
            print("not found!")
    if command == "l":
        for i in range(0, len(names)):
            print(names[i] + "\t" + str(heights[i]) + " cm")
    if command == "min":
        minimum = heights[0]
        for height in heights:
            if height < minimum:
                minimum = height
        print(str(minimum) + " cm")
    if command == "max":
        maximum = heights[0]
        for height in heights:
            if height > maximum:
                minimum = height
        print(str(maximum) + " cm")
    if command == "q":
        break
    if command == "?":
        print("a = add new student")
        print("d = delete student")
        print("l = list students")
        print("q = quit program")
