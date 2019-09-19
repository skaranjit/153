"""
This is the main program that will import methods from fraction module and allow user to read from file and compute airthematic operation for the fraction.

"""
__author__="Suman Karanjit"
__date__ ="03/16/2019"

from modFraction import *
from os.path import *
import tkinter as tk
from tkinter import filedialog
from itertools import islice

def PrintReport(f1,f2,f3,operator):
    """
    Pre-Condiiton: It will take 3 fraction object and one operator(string)
    Post-Condition: Prints in formatted report.

    It will print out the formatted report. 
    """
    print("-"*35)
    print ("{:^7s}{:^2s}{:^7s}{:^2s}{:^7s}".format(str(f1),operator,str(f2)," = ",str(f3)))
    print("*"*35,"\n")
root = tk.Tk()
root.withdraw()
fileName = filedialog.askopenfilename()
while not fileName.endswith(".txt"):
    print("Please select the correct text file")
    fileName = filedialog.askopenfilename()

if __name__ == "__main__":
    myDict = {}
    if isfile(fileName):
    
        with open(fileName,"r") as fileObj:    #opens file with read access
            tmpList = []
            for lines in fileObj:
                lines = lines.strip("\n")
                line = lines.split()
                if line != []:
                    tmpList.append(line)
        fileObj.close()
    else:
        Print("File does not exist")

    if tmpList == []:
        print("Your file does not contain data")
    else:
        try:
                     
            for ct in range(0,len(tmpList),2):
                operator = tmpList[ct+1][0]
                f1 = Fraction(int(tmpList[ct][0]),int(tmpList[ct][1]))
                f2 = Fraction(int(tmpList[ct][2]),int(tmpList[ct][3]))
                if operator == "Add":
                    f3 = (f1+f2)
                    print("*"*35)
                    print("Addition of ", f1, "and", f2,":")
                    PrintReport(f1,f2,f3,"+")
                elif operator == "Sub":
                    f3 = f1-f2
                    print("*"*35)
                    print("Subtraction of ", f1, "and", f2,":")
                    PrintReport(f1,f2,f3,"-")
                elif operator == "Mul":
                    f3 = f1*f2
                    print("*"*35)
                    print("Multiplication of ", f1, "and", f2,":")
                    PrintReport(f1,f2,f3,"*")
                elif operator == "Div":
                    f3 = f1/f2
                    print("*"*35)
                    print("Division of ", f1, "and", f2,":")
                    PrintReport(f1,f2,f3,"÷")
                elif operator == "LessThan":
                    f3 = f1 < f2
                    print("*"*35)
                    print("Is ", f1, "less than", f2,"?")
                    PrintReport(f1,f2,f3,"<")
                elif operator == "GreaterThan":
                    f3 = f1 < f2
                    print("*"*35)
                    print("Is ", f1, "greater than", f2,"?")
                    PrintReport(f1,f2,f3,">")
                elif operator == "Equal":
                    f3 = f1 == f2
                    print("*"*35)
                    print("Is ", f1, "equal to", f2,"?")
                    PrintReport(f1,f2,f3,"==")
                else:
                    print("*"*35)
                    print("\nInvalid Option selected.Please check your file and try again.\n")
                    print("*"*35,"\n")
                    
        
        except:
            print("Invalid Data on file. Please check your file and try again")
        

        
                
        



    
