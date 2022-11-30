sentence = "Příliš žluťoučký kůň úpěl ďábelské ódy"

print(len(sentence))    # délka věty
print(sentence[0])      # první písmeno
print(sentence[-1])     # poslední písmeno

index = -1
while index >= -len(sentence):
    print(sentence[index], end="")
    index -= 1
print()

index = len(sentence) - 1
while index >= 0:
    print(sentence[index], end="")
    index -= 1
print()
