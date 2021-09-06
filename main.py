import lessons.Chemical as Chemical
import lessons.Informate as Informate
import lessons.Math as Math
import lessons.Physics as Physics
from functions import *
def main():
    TerminalClear()
    while True:
        print(line)
        print("1) Chemicals application")
        print("2) Informate application")
        print("3) Math application")
        print("4) Physicals application")
        print("998) Develop")
        print("999) Exit")
        print(line)
        Ans = input("Enter number: ")
        if Ans == "1":
            Ans = ""
            TerminalClear()
            Chemical.ChemicalApplication()
        if Ans == "2":
            Ans = ""
            TerminalClear()
            Informate.InformateApplication()
        if Ans == "3":
            Ans = ""
            TerminalClear()
            Math.MathApplication()
        if Ans == "4":
            Ans = ""
            TerminalClear()
            Physics.PhysicsApplication()
        if Ans == "998":
            Ans = ""
            while True:
                TerminalClear()
                print(line)
                print("1) Chemical")
                print("2) Informate")
                print("3) Math")
                print("4) Physics")
                print("999) exit")
                print(line)
                Ans1 = input("Enter number: ")
                print(line)
                if Ans1 == "1":
                    TerminalClear()
                    Chemical.ChemicalApplication("develop")
                if Ans1 == "2":
                    TerminalClear()
                    Informate.InformateApplication("develop")
                if Ans1 == "3":
                    TerminalClear()
                    Math.MathApplication("develop")
                if Ans1 == "4":
                    TerminalClear()
                    Physics.PhysicsApplication("develop")
                if Ans1 == "999":
                    TerminalClear()
                    Ans1 == ""
                    break
        if Ans == "999":
            Ans = ""
            ProgramExit()
            print("Hello World")
        Ans = ""
main()