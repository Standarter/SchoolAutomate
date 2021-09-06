from lessons.database.DatabasePhysics import *
from functions import *
def PhysicsApplication(Mode="default"):
    while True and Mode == "default":
        print("1)")
        print("999) exit")
        Ans = input("Enter number: ")
        if Ans == "999":
            Ans = ""
            TerminalClear()
            break
    while True and Mode == "develop":
        print(line)
        print("Lesson:", "Physics")
        print(line)
        print("999) exit")
        print(line)
        Ans = input("Enter number: ")
        print(line)
        if Ans == "999":
            Ans = ""
            TerminalClear()
            break