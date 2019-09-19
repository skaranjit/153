askUser = input("Enter a sentence")

ct = 0
for char in askUser:
    if char.isdigit():
        ct += 1

noOfComma = askUser.count(',')

print("Digits: ", ct)
print("Commas: ", noOfComma)

