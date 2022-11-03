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
    newlines.append(line)

with open(file, "w") as f:
    f.writelines(newlines)