import re
import requests
import time
import sys
import requests
import lessons.database.ChemicalElements as ChemicalElementsDB
class Chemical:
    elements = ChemicalElementsDB.elements
    def GetElementByName(self, Name):
        try:
            return self.elements[Name.lower()]
        except:
            return "No element found"
    def GetElementByZ(self, Z):
        DB = self.elements.keys()
        for i in DB:
            if int(self.elements[i]['Z']) == Z:
                return self.elements[i]
        return "Element not found"
    def GetElementByWeight(self, Weight):
        DB = self.elements.keys()
        for i in DB:
            if float(self.elements[i]['weight']) == Weight:
                return self.elements[i]
        return "Element not found"
    def GetElementBySymbol(self, Symbol):
        DB = self.elements.keys()
        for i in DB:
            if self.elements[i]['symbol'] == Symbol:
                return self.elements[i]
        return "Element not found"
    def GetElementZ(self, Element):
        return int(Element['Z'])
    def GetElementSymbol(self, Element):
        return Element['symbol']
    def GetElementName(self, Element):
        return Element['name']
    def GetElementWeight(self, Element):
        return float(Element['weight'])
Chem = Chemical()
Chemicals = Chem.elements

def AllElements(Formula):
    return re.findall("[A-Z][a-z]*[0-9]*", Formula)
def CountElement(Element):
    Count = re.findall("[1-9]{1,3}", Element)
    if len(Count) > 0:
        return int(Count[0])
    else:
        return 1
def GetFactor(Element):
    if re.findall("^[0-9]*", Element)[0] != "":
        return int(re.findall("^[0-9]*", Element)[0])
    else:
        return 1
def GetElement(Element):
    return re.findall("[A-Z][a-z]*", Element)[0]
def CalculateFormula(Formula, roundTo=2):
    Result = 0
    StepOne = AllElements(Formula)
    for i in StepOne:
        ElementSymbol = GetElement(i)
        Element = Chem.GetElementBySymbol(ElementSymbol)
        Weight = Chem.GetElementWeight(Element)
        Result += (Weight*CountElement(i))
    print(Formula)
    return round(GetFactor(Formula)*Result, roundTo)
def ElementInfo(Formula):
    StepOne = CalculateFormula(Formula)
    StepTwo = AllElements(Formula)
    for i in StepTwo:
        ElementSymbol = GetElement(i)
        Element = Chem.GetElementBySymbol(ElementSymbol)
        Weight = Chem.GetElementWeight(Element)
        print("Element (" + GetElement(i) + "):", str(round(Weight*CountElement(i)/StepOne*100, 2)) + "%")
def GetHttpChemicalFormula(Formula):
    Formula = Formula.replace("+", "%2B")
    Text = requests.get("https://chemequations.com/ru/?s=" + Formula + "&ref=input").text
    Text = re.findall("""<title>.*</title>""", Text)[0]
    return Text

def ChemicalParce(Text):
    Text = re.sub("""<title>""", "", Text)
    Text = re.sub("""</title>""", "", Text)
    Text = re.sub("""Вычисленное уравнение""", "", Text)
    Text = re.sub("""Химические Уравнения oнлайн!""", "", Text)
    Text = re.sub("""&rarr;""", "=>", Text)
    Text = re.sub(""" [|] """, "", Text)
    Text = re.sub(""" - """, "", Text)
    Text = re.sub("""[:][+]""", "(+)", Text)
    Text = re.sub("""[:][-]""", "(-)", Text)
    Text = re.sub(""" - """, "", Text)
    return Text