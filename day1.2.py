# Idee: ersetze der Strings pro Zeile mit den korrespondierenden Zahlen
# zuerst die überschneidenden Ziffern ersetzen
# bilden einer 

substitutes = {
    "oneight": 18,
    "twone": 21,
    "threeight": 38,
    "fiveight": 58,
    "sevenine": 79,
    "eightwo": 82,
    "eightree": 83,
    "nineight": 98,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

sumofcalvals = 0


def wortlauf(word, reihenfolge):
    """
    durchläuft einen String und gibt ihn aus
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
    print(linienzahl)
    return linienzahl

with open("AOC_day1_input.txt", "r") as file:
    # read file line by line and output the lines
    for line in file:
        line = line.strip()
        print(line)
        
        for i in substitutes: 
            line = line.replace(i, str(substitutes[i]))
        
        print(line)
        sumofcalvals = sumofcalvals + twodigitnumber(line)
        print(" ")
        
print("Das Ergebnis lautet:", sumofcalvals)
