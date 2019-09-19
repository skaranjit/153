Sent = input("Enter Sentence:")
tmpList = []
num =0
wordList = Sent.split()
numofCapWord = 0
numofCapLet = 0
print(wordList)
for word in wordList:
    x = 0
    for char in word:
        if char.isupper():
            numofCapLet += 1
            if char in word:
                x += 1
    if x > 0:
        numofCapWord += 1


print(numofCapWord," words with uppercase")
print(numofCapLet," uppercase letters")

