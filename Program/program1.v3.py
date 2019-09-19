"""
This progam consists of the function to check on SSN and returns true. The main
part of the program will ask for user to enter ssn in correct format until they
done. ALso will calll the function , append it to the list and print the report accordingly.

"""
__author__="Suman Karanjit"
__date__= "Jan 21,2019"



####################Function to check if user enter correct ssn#################
def isValidSSN(ssn):
    if len(ssn) == 11:   ###Checks if the entered number length is 11
        if ssn[3] == '-' and ssn [6] == '-': ##Check if hyphens are in correct place
            if ssn[0:3].isdigit() and\
               ssn[4:6].isdigit() and\
               ssn[7:11].isdigit(): ###Checks digits are in correct place
                if int(ssn[0]) != 0: ##checks if the first number is not '0'
                    return True
                else: return False
            else: return False
        else: return False
    else:
        return False

################################################################################

######################################MAIN######################################

InputSSN = input ("Enter SSN or type 'Done' to Exit: ")

ssnList = []
while InputSSN.lower() != "done":
    if isValidSSN(InputSSN):
        ssnList.append([InputSSN,isValidSSN(InputSSN)])
    else:
        ssnList.append([InputSSN,isValidSSN(InputSSN)])
    InputSSN = input("Enter SSN or type 'Done' to Exit: ")
    
    
##################################Printing Report##############################
if ssnList != []:
    print("The List of SSN and Values: \n",ssnList,'\n\n\n')

    print('{:50}{}'.format("Social Security Number","Valid"))
    print('{0:-^80}\n{0:-^80}'.format("",""))
    for sublist in ssnList:
        if sublist[1] == True:
            print('{:50}{}'.format(sublist[0],"Yes"))
        else:
            print('{:50}{}'.format(sublist[0],"No"))
        
###############################################################################
###############################################################################


