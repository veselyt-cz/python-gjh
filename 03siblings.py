print("Kolik je ti let?")
age1 = int(input())

print("Mas nejakeho sourozence?")
if input() == "ANO":
    print("Kolik je mu let?")
    age2 = int(input())

    if age2 > age1:
        print("Takze je o " + str(age2 - age1) + " let starsi nez ty.")
    elif age1 > age2:
        print("Takze je o " + str(age1 - age2) + " let mladsi nez ty.")
    else:
        print("Takze jste stejne stari - nejste nahodou dvojcata?")

else:
    print("Takze jsi jedinacek.")
