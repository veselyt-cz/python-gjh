print("Enter your age:")
age = int(input())

if age < 0:
    print("That is not your age!")
elif age < 15:
    print("You are child.")
elif age < 18:
    print("You are junior.")
elif age < 27:
    print("You are student.")
elif age < 65:
    print("You are adult.")
else:
    print("You are senior.")
