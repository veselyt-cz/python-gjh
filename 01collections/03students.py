names = ["Tomas", "Kuba", "Vojta"]
heights = [173, 185, 181]

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
            index = names.index(name)
            names.pop(index)
            heights.pop(index)
        except ValueError:
            print("not found!")
    if command == "f":
        name = input("name: ")
        for i in range(0, len(names)):
            if names[i] == name:
                print(str(heights[i]) + " cm")
    if command == "l":
        for i in range(0, len(names)):
            print(names[i] + "\t" + str(heights[i]) + " cm")
    if command == "avg":
        total = 0
        for height in heights:
            total += height
        average = round(total / len(heights), 1)
        print(str(average) + " cm")
    if command == "var":
        total = 0
        for height in heights:
            total += height
        average = total / len(heights)
        for height in heights:
            total += (height - average) ** 2
        variance = round(total / (len(heights) - 1), 1)
        print(str(variance))
    if command == "min":
        name = names[0]
        minimum = heights[0]
        for i in range(0, len(names)):
            if heights[i] < minimum:
                name = names[i]
                minimum = heights[i]
        print(name + " " + str(minimum) + " cm")
    if command == "max":
        maximum = 0
        for i in range(0, len(names)):
            if heights[i] > heights[maximum]:
                maximum = i
        print(names[maximum] + " " + str(heights[maximum]) + " cm")
    if command == "q":
        break
    if command == "?":
        print("a = add new student")
        print("d = delete student")
        print("l = list students")
        print("q = quit program")
