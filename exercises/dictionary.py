#StuDict Associates id with a list
#Containing fullName, Major, gpa
#ex: { id: [Name,maj,gpa]}

stuDict = {}
id = input("ID: ")

while id.upper() != "DONE":
    name = input("Name: ")
    major = input("Major: ")
    gpa = input("Gpa: ")
    stuDict[id] = [name,major,gpa]
    id = input("id: ")


##Print the Dictionary###
for id in stuDict:
    tmpList = stuDict[id]
    name = tmpList[0]
    major = tmpList[1]
    gpa = [tmpList[2]]
    
