sumofcalvals = 0

def wortlauf(word, reihenfolge):
    """
    durchläuft einen String und gibt in aus
    """
    buchstabenliste = []
    for buchstabe in word[::reihenfolge]:
        if buchstabe.isdigit():
            buchstabenliste.append(buchstabe)
    buchstabenliste.append("0")
    return buchstabenliste[0]

def twodigitnumber(word):
    """
    Suchen der ersten Zahl und der letzten Zahl eines Strings
    """
    linienzahl = int(wortlauf(word, 1) + wortlauf(word, -1)) 
    return linienzahl

with open("AOC_day1_input.txt", "r") as file:
    # read file line by line and output the lines
    for line in file:
        line = line.strip()
#        print(line)
#        print(twodigitnumber(line))
        sumofcalvals = sumofcalvals + twodigitnumber(line)

print(sumofcalvals)
