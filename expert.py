from solvers import *

def parseInput(inp:str):
    l = inp.split(" ")
    intention = l[0].lower()
    inputs = l[1:]

    if intention == "wires":
        num = int(l[1])

        if num < 5:
            wires = l[2:]
            return solveWires(num,wires)
        elif num == 5:
            return solveWires(5,None,l[2].lower())
        
    if intention == "button":
        color = l[1]
        text = l[2]
        return solveButton(color,text)
    
    if intention == "hex" or intention == "hexadecimal":
        return solveHexadecimal("".join(inputs))
    
    if intention == "keypads" or intention == "keys":
        return solveKeypads(inputs)
    
    if intention == "binary" or intention == "b" or intention == "bin":
        if len(inputs) == 1: lit = [*inputs[0]]
        else: lit = [int(k) for k in inputs]
        if lit[0] == 0: lit = []
        return solveBinary(lit)
    
    if intention == "mathematics" or intention == "math":
        return solveMathematics(l[1],l[2])
    
    if intention in ["colorcode","colors","cc"]:
        #lights will be written as all words,
        #display will be written as all one word

        lights = inputs[:-1]
        display = [*inputs[-1]]

        for ind,i in enumerate(lights):
            if i == "white":
                lights[ind]="w"
            if i == "blue":
                lights[ind]="b"
            if i == "yellow":
                lights[ind]="y"


        return solveColorCode(lights,display)
    
    if intention in ["multibuttons","multi","mb"]:
        return solveMultiButtons(l[1])
    
    if intention == "timing":
        n = l[1]
        l = l[2]
        return solveTiming(n,l)
    
    if intention == "tiles":
        return solveTiles(inputs)
    
    if intention == "morse":
        return translateMorse(inputs)
    
    if intention == "serial":
        return findMorseSerial(l[1])




while True:
    k = input("Tell me:\n")
    if k.lower().replace(" ","") == "stop":
        break

    try:
        answer = parseInput(k)
    except:
        print("An error occurred.")
    print("\n"+str(answer)+"\n")
