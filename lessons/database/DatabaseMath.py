from functions import *
import math
import decimal
import random

Int = decimal.Decimal

class MathClassDF:
    def __init__(self):
        decimal.getcontext().prec = 4
        self.RoundTo = 4
        dx = Int("1")/Int("10")**(self.RoundToDX)
    RoundTo = 4
    RoundToDX = 2
    TrigonometryMode = "degrees"
    dx = Int("1")/Int("10")**(RoundToDX)
    def MathFunc(self, Formula, Vars={"x"}):
        for Veriable in Vars.keys():
            #print("X", Vars[Veriable])
            Formula = str(Formula).replace(Veriable, str(Vars[Veriable]))
            #print(Formula)
        Result = Int(eval(Formula))
        return Int(self.IntConvert(Result))
    def Differencial(self, Formula, x):
        #print(self.MathFunc(Formula, {"x": x + self.dx}))
        #print(self.MathFunc(Formula, {"x": x}))
        return Int(self.MathFunc(Formula, {"x": x + self.dx})) - Int(self.MathFunc(Formula, {"x": x}))
    def Derived(self, Formula, x):
        return Int(self.Differencial(Formula, x)/self.dx)
    def NewtonMethod(self, Formula, Result, x = 1, accuracy=RoundTo):
        x = Int(x)
        #print("X:", x)
        while abs(self.MathFunc(Formula + "-("  + str(Result) + ")", {"x": x})) > 1/10**(accuracy - 2):
            #print("Func:",self.MathFunc(Formula + "-("  + str(Result) + ")", {"x": x}))
            #print("FuncDerived:", self.Derived(Formula + "-("  + str(Result) + ")", x))
            #print("X:",x)
            x = x - self.MathFunc(Formula + "-("  + str(Result) + ")", {"x": x})/(self.Derived(Formula + "-("  + str(Result) + ")", x) + Int("0.01"))
        return Int(x)
    def IntConvert(self, number):
        if MathClass.is_integer_decimal(number):
            return Int(number)
        else:
            return Int(number)
    def sin(self, x):
        if self.TrigonometryMode == "degrees":
            x = Int(math.radians(x))
        return Int(str(round(math.sin(x), self.RoundTo)))
    def cos(self, x):
        if self.TrigonometryMode == "degrees":
            x = Int(math.radians(x))
        return Int(str(round(math.cos(x), self.RoundTo)))
    def tg(self, x):
        return Int(str(round(self.sin(x)/self.cos(x), self.RoundTo)))
    def ctg(self, x):
        return Int(str(round(self.cos(x)/self.sin(x), self.RoundTo)))
    def sqrt(self, x):
        return Int(x).sqrt()
    def is_integer_decimal(self, x):
        return True if x % 1 == 0 else False
    def FunctionParcer(self, Formula):
        FormulaResult = Formula.split("=")[0]
        return [FormulaResult, Int(Formula.split("=")[1])]

MathClass = MathClassDF()
is_integer_decimal = MathClass.is_integer_decimal

sin = MathClass.sin
cos = MathClass.cos
tg = MathClass.tg
ctg = MathClass.ctg
sqrt = MathClass.sqrt


def Solve_Equation(Formula, accuracy = MathClass.RoundTo):
    Data = MathClass.FunctionParcer(Formula)
    Result = MathClass.NewtonMethod(Data[0], Data[1], x = random.random(), accuracy=accuracy)
    return Result
def CalculateMath(Formula):
    return eval(Formula)
def QuadraticEquations():
    print("Equation: ax**2 + bx + c = 0")
    print(line)
    a = Int(input("Enter a: "))
    b = Int(input("Enter b: "))
    c = Int(input("Enter c: "))
    print(line)
    d = Int(b**2 - 4*a*c)
    if d > 0:
        if MathClass.is_integer_decimal(d.sqrt()):
            x1 = (-b + d.sqrt())/Int(2*a)
            x2 = (-b - d.sqrt())/Int(2*a)
        else:
            x1 = "(-{0} + sqrt({1}))/({2})".format(MathClass.IntConvert(b), MathClass.IntConvert(d), MathClass.IntConvert(2*a))
            x2 = "(-{0} - sqrt({1}))/({2})".format(MathClass.IntConvert(b), MathClass.IntConvert(d), MathClass.IntConvert(2*a))
        print("First root:", x1)
        print("Second root:", x2)
    elif d == 0:
        print("Root:", -b/(2*a))
    elif d < 0:
        print("No root's in real field")
    print(line)
    input("Press Enter to continue...")
    TerminalClear()