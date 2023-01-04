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
        print(names)
        print(heights)
    if command == "q":
        break
    if command == "?":
        print("a = add new student")
        print("d = delete student")
        print("l = list students")
        print("q = quit program")
