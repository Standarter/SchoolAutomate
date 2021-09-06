import math
from functions import *
def FormatString(Number):
    Text = Number
    Text = Text.replace("kb", "*8*1024")
    Text = Text.replace("mb", "*8*1024**2")
    Text = Text.replace("gb", "*8*1024**3")
    Text = Text.replace("byte", "*8")
    Text = Text.replace("kilobyte", "*8*1024")
    Text = Text.replace("megabyte", "*8*1024**2")
    Text = Text.replace("gigabyte", "*8*1024**3")
    Text = Text.replace("b", "*8")
    return Text
def ConvertString(String):
    try:
        return str(float(String))
    except:
        return str(len(String))
def ConvertNumber(Number, output):
    if output == "":
        output = "bit"
    output = output.lower()
    if output == "bit":
        return str(float(Number))
    if output == "b" or output == "byte":
        return str(float(Number)/8) + "b"
    if output == "kb" or output == "kilobyte":
        return str(float(Number)/8) + "kb"
    if output == "mb" or output == "megabyte":
        return str(float(Number)/8) + "mb"
    if output == "gb" or output == "gigabyte":
        return str(float(Number)/8) + "gb"
def InformateTask():
    isN = False
    isI = False
    print("1 byte = 1 b")
    print("1 kilobyte = 1 kb")
    print("1 megabyte = 1 mb")
    print("1 gigabyte = 1 gb")
    print(line)
    Out = input("Enter output format: ")
    print(line)
    print("Data:")
    try:
        N = str(eval(ConvertString(FormatString(input("Enter N (How meny char we have in alphabet): ")).lower())))
    except:
        N = ""
    try:
        i = str(eval(FormatString(input("Enter i (How much cost one character): ").lower())))
    except:
        i = ""
    try:
        k = str(eval(FormatString(input("Enter k (How meny char we have in text): ").lower())))
    except:
        k = ""
    try:
        I = str(eval(FormatString(input("Enter I (Text size): ").lower())))
    except:
        I = ""
    print("Solve:")
    if I != "":
        if k != "":
            i = float(I)/float(k)
            print("i = I/k = {0}b/{1} = {2}".format(I, k, i))
            if i != "":
                N = 2**int(i)
                print("N = 2**i = 2**{0} = {1}".format(i, N))
                isN = True
        if i != "":
            k = float(I)/float(i)
            print("k = I/i = {0}/{1} = {2}".format(I,i,k))
    if N != "":
        i = math.log2(float(N)) if math.log2(float(N)).is_integer() else int(math.log2(float(N))) + 1
        if math.log2(float(N)).is_integer():
            print("N = 2**i => i = {0}".format(i))
        else:
            print("2**{0} < {1} => i = {2}".format(int(math.log2(float(N))), N, int(math.log2(float(N))) + 1))
    if k != "" and isI == False:
        if i != "":
            I = float(i)*float(k)
            print("I = ik = {0}*{1} = {2}".format(i,k,I))
            isI = True

    if i != "" and isN == False:
        if k != "" and isI == False:
            I = float(i)*float(k)
            print("I = ik = {0}*{1} = {2}".format(i,k,I))
        N = 2**int(i)
        print("N = 2**i = 2**{0} = {1}".format(i, N))
    print("Answers:")
    print("N:", N)
    print("i:", i)
    print("k:", k)
    print("I:", ConvertNumber(I, Out))
