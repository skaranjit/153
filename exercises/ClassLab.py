myScores = [85,90,65]
myCurvedList = [score+10 for score in myScores]
print(myCurvedList)

#######################
myTests = [10,98,90,80]
myATests = [sc for sc in myTests if sc>=90]
print(myATests)
###########################
Sentences = "The quick brown fox"
wordList = Sentences.split()
newList = [w.title() for w in wordList]
print(newList)
######################################
tmp = "My attic is full of everything including furtiture"
newList = [wd[0] for wd in tmp.split() if wd[0].lower() not in "aeiou"]

print(newList)

###############################
def calcLetterGrade(sc):
    if sc >= 90: return 'A'
    elif sc >= 80: return 'B'
    elif sc >=70: return 'C'
    elif sc >= 60: return 'D'
    else: return 'F'

scList = [100,81,95,67,40,78]
gradeList = [calcLetterGrade(sc) for sc in scList]
print(gradeList)
