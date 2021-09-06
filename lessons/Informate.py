from lessons.database.DatabaseInformate import *
from functions import *
def InformateApplication(Mode="default"):
    while True and Mode == "default":
        print(line)
        print("1) Informational Task (INik)")
        print("999) exit")
        print(line)
        Ans = input("Enter number: ")
        print(line)
        if Ans == "1":
            Ans = ""
            InformateTask()
            input("Press Enter to continue...")
            TerminalClear()
        if Ans == "999":
            Ans = ""
            TerminalClear()
            break
    while True and Mode == "develop":
        print(line)
        print("Lesson:", "Informate")
        print(line)
        print("999) exit")
        print(line)
        Ans = input("Enter number: ")
        print(line)
        if Ans == "999":
            Ans = ""
            TerminalClear()
            break