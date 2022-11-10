import sys


file = sys.argv[1]

with open(file, "r") as f:
    lines = f.readlines()

newlines = []

for line in lines:
    if "M1345" in line:
        line = line.replace("Jovanović, Nataša", "Jovanović2, Nataša")
        line = line.replace("M1345", "M782")
    if "M781" in line:
        line = line.replace("Jovanović1, Nataša", "Jovanović, Nataša")

    if "M231" in line:
        line = line.replace("Nikolić, Dragan", "Nikolić2, Dragan")
    if "M1278" in line:
        line = line.replace("Nikolić, Zoran", "Nikolić2, Zoran")
    if "M1022" in line:
        line = line.replace("Stojanović-Plavšić, Snežana", "Stojanović-Plavšić2, Snežana")
    if "M248" in line:
        line = line.replace("Todorović, Dragan", "Todorović2, Dragan")
    if "M1364" in line:
        line = line.replace("Krstić, Nenad", "Krstić2, Nenad")
    if "M1369" in line:
        line = line.replace("Lazić, Nikola", "Lazić2, Nikola")
    if "M1455" in line:
        line = line.replace("Urošević, Milan", "Urošević2, Milan")
    if "M1471" in line:
        line = line.replace("Juhas, Atila","Juhas2, Atila")
    if "M1474" in line:
        line = line.replace("Marković, Predrag","Marković2, Predrag")
        
    newlines.append(line)

with open(file, "w") as f:
    f.writelines(newlines)