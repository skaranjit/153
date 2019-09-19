sc = input("Score --- Done to quit")
scList = []

while sc.upper() != "DONE":

    scList.append(sc)
    sc = input("Score --- Done to quit")


#scList will be a list of strings
print(scList)


#List Comprehension

neList = [int(item)+10 for item in scList if int(item)<60]
print(neList)

neList = [[item,int(item)+10] for item in scList if int(item)<60]
print(neList)



sent = "hi there goodbye"
vowels = "aeiou"

vowelList = [item for item in sent if item.lower() in vowels]
print(vowelList)
