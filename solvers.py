import re

def solveWires(numberOfWires,wires,lightColor=None):
    if numberOfWires == 3:
        if "red" not in wires:
            return "first wire"
        if "white" in wires:
            return "second wire"
        if "blue" in wires:
            return "last wire"
    if numberOfWires == 4:
        if "green" not in wires:
            return "first wire"
        elif "blue" not in wires:
            return "second wire"
        elif "white" not in wires:
            return "third wire"
        else:
            return "last wire"
    if numberOfWires == 5:
        if lightColor == "red": return "first wire"
        elif lightColor == "green": return "second wire"
        elif lightColor == "blue": return "third wire"
        elif lightColor == "yellow": return "fourth wire"
        else: return "last wire"

def solveButton(color,text):
    if color == "blue" and text == "detonate":
        return "press once then down"
    elif color == "red":
        return "press twice then down"
    elif text == "abort":
        return "press three times then up"
    elif color == "white":
        return "press four times then up"
    
def solveHexadecimal(string): #capitalization does not matter
    s = bytes.fromhex(string.replace(" ",""))
    parsed = s.decode("ASCII")
    return parsed

def solveKeypads(keys):
    keys = [int(k) for k in keys]
    k1,k2,k3,k4 = keys[0],keys[1],keys[2],keys[3]

    x = 0
    #key 1
    if k1<10: x=15
    elif k1>10 and k1<20: x=20
    elif k1>20 and k1<80: x=30
    else: x=10
    #key 2
    if k2<10: x+=10
    elif k2>10 and k2<20: x*=2
    elif k2>20 and k2<80: x*=3
    else: x-=10
    #key 3
    if k3<10: x*=2
    elif k3>10 and k3<20: x*=3
    elif k3>20 and k3<80: x-=5
    #key 4
    if k4<10: x*=2
    elif k4>10 and k4<20: x+=20
    elif k4>20 and k4<80: x+=50
    else: x*=3

    y = sum(keys)/2
    z = x-y

    if z <= 0:
        return "TL TR BL BR"
    elif z >= 0.5 and z <= 19.5:
        return "TL TR BR BL"
    elif z >= 20 and z <= 49.5:
        return "BR BL TR TL"
    elif z >= 50 and z <= 89.5:
        return "BL TL BR TR"
    elif z >= 90:
        return "TR BL TL BR"
    
def solveBinary(lit): #takes in a list of lit numbers
    if len(lit) == 0: return "red once"
    elif 2 in lit and 7 not in lit: return "red twice"
    elif 1 in lit and 2 in lit: return "red 3 times"
    elif 1 not in lit and 7 not in lit: return "red 4 times"
    elif 7-len(lit)>3: return "red 7 times"
    elif len(lit)>5: return "red 8 times"
    else: return "red 10 times"

def solveMathematics(string1,string2):
    replacementDictionary = {"A":"1","B":"3","C":"7","D":"2","E":"4",
                             "F":"5","G":"6","H":"0","I":"8","J":"9"}
    
    string1 = string1.upper()
    string2 = string2.upper()

    for initial, replacement in replacementDictionary.items():
        string1 = string1.replace(initial, replacement)
        string2 = string2.replace(initial, replacement)

    a = 10*int(string1[0])+int(string1[1])
    b = 10*int(string2[0])+int(string2[1])

    return a*b

def solveColorCode(lights,display):
    lights = [l.lower() for l in lights]
    display = [l.lower() for l in display]

    y = 0
    for l in lights:
        if l == "b": y+=1
        if l == "y": y+=2
        if l == "w": y+=3
    
    x = 0
    for d in display:
        if d == "r": x+=1
        if d == "b": x+=2
        if d == "g" or d == "y": x+=3
        if d == "w": x+=4

    return x-y if x-y>0 else 0

def solveMultiButtons(string:str):
    string = [*string]
    code = [int(k) for k in string]

    s = ""
    if code[0] <6: s+="red, "
    else: s+= "orange, "

    if code[1] <6: s+="yellow, "
    else: s+= "green, "

    if code[2] <6: s+="blue, "
    else: s+= "purple, "

    s+="columns "

    if code[3] < 7: return s+"231"
    if code[4] < 7: return s+"321"
    if code[5] > 5: return s+"123"
    return s+"132"

def solveTiming(numbers,letters:str):
    a = sum([int(k) for k in [*numbers]])
    b = 0

    letters = letters.upper()
    for _, v in enumerate(letters):
        if v == "A": b += 4
        elif v == "B": b += 3
        elif v == "C": b += 7
        elif v == "D": b += 9

    c=a*b
    if c <= 59: return "white"
    elif c >= 60 and c <= 99: return "red"
    elif c >= 100 and c <= 199: return "yellow"
    elif c >= 200 and c <= 299: return "green"
    elif c >= 300: return "blue"
    # maximum is 324 on "99 DD" which means the higher colors aren't attainable

def solveTiles(colors):
    total = 0
    for c in colors:
        if c in ["red","r"]: total+=1
        if c in ["green","g"]: total+=9
        if c in ["blue","b"]: total+=7
        if c in ["yellow","y"]: total+=2
        if c in ["pink","p","i"]: total+=6
        if c in ["white","w"]: total+=5
    return total

def findMorseSerial(serial:str):
    serial = [*serial.upper()]
    if "A" in serial: return "yellow"
    if "6" in serial or "D" in serial or "8" in serial: return "blue"
    if "I" in serial or "1" in serial: return "yellow"
    return "blue"