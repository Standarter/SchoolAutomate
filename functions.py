import platform
import os

line = "########################"
def TerminalClear():
    ThisSystem = platform.system()
    if ThisSystem == "Windows":
        os.system("cls")
    if ThisSystem == "Linux":
        os.system("clear")
def ProgramExit():
    TerminalClear()
    exit()