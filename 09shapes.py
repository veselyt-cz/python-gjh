width = 9
height = 5

j = 0
while j < height:
    i = 0
    while i < width:
        print("*", end="")
        i += 1
    print()
    j += 1

i = 1
j = height - 1
while i <= height:
    print(j * " " + i * "*")
    i += 1
    j -= 1
