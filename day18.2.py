## Teil 2, Matrixgröße berechnen
## UNSUCCESSFUL


import numpy as np

file = "AOC_day18_input.txt"
document = []


def einlesen(filename):
    """
    liest alle Zeilen eines Textfiles ein und speichert jede einzelne Zeile in einer Liste
    """
    with open(filename, "r") as file:
        # read file line by line and output the lines
        for line in file:
            line = line.strip()
            document.append(line)
    return document


def matrix_groesse(inputmatrix):
    zeilen = 0
    spalten = 0 
    max_spalte = 0
    max_zeile = 0

    for line in inputmatrix:
        if line[0] == "R":
            spalten = spalten + int(line[1])
        elif line[0] == "L":
            spalten = spalten - int(line[1])
        elif line[0] == "D":
            zeilen = zeilen + int(line[1])
        elif line[0] == "U":
            zeilen = zeilen - int(line[1])

        # ermittelt jeweils die Verschiebung des maxwerts
        if spalten > max_spalte:   
            max_spalte = spalten
        if zeilen > max_zeile:
            max_zeile = zeilen

    max_zeile = max_zeile + 1
    max_spalte = max_spalte + 1
    
    return max_zeile, max_spalte


def teil2baggerbewegungen(document):
    baggermatrix = []

    for line in document:
        bw = []
        hexzahl = 0
        intzahl = 0

        line2 = line.split(" (")
        baggerbew2 = line2[1].split(" ")
        baggerbew3 = baggerbew2[0]

        direction = richtung(baggerbew3[-2:-1])
        bw.append(direction)

        hexzahl = baggerbew3[1:6]
        intzahl = int(hexzahl, 16)
        bw.append(intzahl)

        baggermatrix.append(bw)

    return baggermatrix   


einlesen(file)




# teilen der Baggerbewegungsliste
### das hier kann ich gleich löschen und durch die neue Liste ersetzen
baggerbewegungen = []
for line in document:
    line2 = line.split(" (")
    baggerbew = line2[0].split(" ")
    baggerbewegungen.append(baggerbew)
    
#print("alte BW", baggerbewegungen)
baggerbewegungen = teil2baggerbewegungen(document)

print("Hexcodes Baggerbewegungen:", baggerbewegungen)

#ermittelt die erforderliche Größe der leeren Matrix
zeilen, spalten = matrix_groesse(baggerbewegungen)
print("Matrix ist", zeilen, "x", spalten, "groß")




