from lessons.database.DatabaseChemical import *
from functions import *

ChemicalDB = Chemical()

def ChemicalApplication(Mode="default"):
    while True and Mode == "default":
        print(line)
        print("Lesson:", "Chemical")
        print(line)
        print("1) Chemestry molecular calculator")
        print("2) Chemestry molecular information")
        print("3) Chemestry element search")
        print("4) Chemestry search (Chemecal Reaction)")
        print("999)")
        print(line)
        Ans = input("Enter number: ")
        print(line)
        if Ans == "exit" or Ans == "999":
            Ans = ""
            TerminalClear()
            break
        if Ans == "1":
            Ans = ""
            while True:
                Formula = input("Enter chemical formula: ")
                if Formula == "exit":
                    TerminalClear()
                    break
                else:
                    print("Molar mass:", CalculateFormula(Formula))
                    print(line)
        if Ans == "2":
            Ans = ""
            while True:
                Formula = input("Enter chemical formula: ")
                if Formula == "exit":
                    TerminalClear()
                    break
                else:
                    ElementInfo(Formula)
                    print(line)
        if Ans == "3":
            Ans = ""
            Ans1 = ""
            while Ans1 not in []:
                print("1) Search by Z")
                print("2) Search by Mass")
                print("3) Search by Name")
                print("4) Search by Symbol")
                print(line)
                Ans1 = input("Enter number: ")
                print(line)
                if Ans1 == "1":
                    Ans2 = int(input("Enter element Z: "))
                    print(line)
                    ElementItem = str(ChemicalDB.GetElementByZ(Ans2)).replace(", ", ",\n")
                    print(ElementItem)
                    print(line)
                if Ans1 == "2":
                    Ans2 = float((input("Enter element Mass: ")))
                    print(line)
                    ElementItem = str(ChemicalDB.GetElementByWeight(Ans2)).replace(", ", ",\n")
                    print(ElementItem)
                    print(line)
                if Ans1 == "3":
                    Ans2 = input("Enter element Name: ")
                    print(line)
                    ElementItem = str(ChemicalDB.GetElementByName(Ans2)).replace(", ", ",\n")
                    print(ElementItem)
                    print(line)
                if Ans1 == "4":
                    Ans2 = input("Enter element symbol: ")
                    print(line)
                    ElementItem = str(ChemicalDB.GetElementBySymbol(Ans2)).replace(", ", ",\n")
                    print(ElementItem)
                    print(line)
        if Ans == "4":
            Ans = ""
            while True:
                Formula = input("Enter chemical reaction: ")
                if Formula == "exit":
                    TerminalClear()
                    break
                else:
                    Text = GetHttpChemicalFormula(Formula)
                    Text = ChemicalParce(Text)
                    print("Searched reaction: ", Text)
                    print(line)
    while True and Mode == "develop":
        print(line)
        print("Lesson:", "Chemical")
        print(line)
        print("999) exit")
        print(line)
        Ans = input("Enter number: ")
        print(line)
        if Ans == "999":
            Ans = ""
            TerminalClear()
            break