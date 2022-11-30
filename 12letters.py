message = input()

index = 0
while index < len(message):
    letter = message[index]
    code = ord(letter)
    if code >= 65 and code <= 90:
        print(code - 64, end=" ")
    if code >= 97 and code <= 122:
        print(code - 96, end=" ")
    index += 1
