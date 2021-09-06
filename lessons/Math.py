from lessons.database.DatabaseMath import *
from functions import *
from math import sin, cos, sqrt
def MathApplication(Mode="default"):
    while True and Mode == "default":
        print(line)
        print("Lesson:", "Math")
        print(line)
        print("1) Quadratic Equations (REAL)")
        print("2) Calculate")
        print("3) Solve equations (Normal)")
        print("998) settings")
        print("999) exit")
        print(line)
        Ans = input("Enter number: ")
        print(line)
        if Ans == "1":
            Ans = ""
            QuadraticEquations()
        if Ans == "2":
            Ans = ""
            Formula = input("Enter formula: ")
            Result = CalculateMath(Formula)
            print("Formula result:", Result)
            input("Press Enter to continue...")
            TerminalClear()
        if Ans == "3":
            Ans = ""
            Formula = input("Enter formula: ")
            Result = Solve_Equation(Formula, MathClass.RoundTo)
            print("Variable x is:", Result)
            print(line)
            input("Press Enter to continue...")
            TerminalClear()
        if Ans == "998":
            Ans = ""
            while True:
                TerminalClear()
                print(line)
                print("Section: Settings")
                print(line)
                print("1) Trigonometry mode:", MathClass.TrigonometryMode)
                print("2) Round to:", decimal.getcontext().prec - 1)
                print("3) DX accuracy:", MathClass.RoundToDX)
                print("4) dx:", MathClass.dx)
                print("999) exit")
                print(line)
                Ans1 = input("Enter number: ")
                print(line)
                if Ans1 == "1":
                    print("1) Degrees")
                    print("2) Radians")
                    Ans2 = ""
                    while Ans2 not in ["1", "2"]:
                        Ans2 = input("Enter number: ")
                    if Ans2 == "1":
                        MathClass.TrigonometryMode = "degrees"
                    elif Ans2 == "2":
                        MathClass.TrigonometryMode = "radians"
                    Ans2 == ""
                if Ans1 == "2":
                    Ans1 = ""
                    decimal.getcontext().prec = int(input("Enter new RoundTo: ")) + 1
                    MathClass.RoundTo = decimal.getcontext().prec
                if Ans1 == "3":
                    Ans1 = ""
                    MathClass.RoundToDX = Int("1")/Int("10")**Int(input("Enter new dx accuracy: "))
                if Ans1 == "999":
                    Ans = ""
                    TerminalClear()
                    break
        if Ans == "999":
            Ans = ""
            TerminalClear()
            break
    while True and Mode == "develop":
        print(line)
        print("Lesson:", "Math")
        print(line)
        print("1) Function Test")
        print("2) Newton Method")
        print("3) Differencial")
        print("4) Derived")
        print("999) exit")
        print(line)
        Ans = input("Enter number: ")
        print(line)
        if Ans == "1":
            Ans = ""
            Result = MathClass.MathFunc("x+1", {"x": 1})
            print("Function result:",Result)
            input("Press Enter to continue...")
            TerminalClear()
        if Ans == "2":
            Ans = ""
            Result = MathClass.NewtonMethod("x**2", Int("2"), x=Int("1"))
        if Ans == "3":
            Ans = ""
            print("dx:", MathClass.dx)
            Result = MathClass.Differencial("sin(x)", 1)
            print(Result)
            Result = MathClass.Differencial("sin(x)", 2)
            print(Result)
            Result = MathClass.Differencial("sin(x)", 3)
            print(Result)
            Result = MathClass.Differencial("sin(x)", 4)
            print(Result)
            Result = MathClass.Differencial("sin(x)", 5)
            print(Result)
        if Ans == "4":
            Ans = ""
            Result = MathClass.Derived("sin(x)", 1)
            print("Derived:", Result)
            Result = MathClass.Derived("sin(x)", 2)
            print("Derived:", Result)
            Result = MathClass.Derived("sin(x)", 3)
            print("Derived:", Result)
            Result = MathClass.Derived("sin(x)", 4)
            print("Derived:", Result)
            Result = MathClass.Derived("sin(x)", 5)
            print("Derived:", Result)
        if Ans == "999":
            Ans = ""
            TerminalClear()
            break