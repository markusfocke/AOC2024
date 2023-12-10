# AOC, Day 10, Teil 2

import numpy as np

last_pos = np.array([14, 34])   # einfach so festgelegt, sollte kein Problem erzeugen, er nimmt einfach einen weg

file = "AOC_day10_input_bsp4.txt"
document = []
document2 = []

spalte = 0
fund_zeile = 0
suchzeichen = "S"
fund_spalte = 0
find = []
zeilen_no = 0
rundlauf = 0
schritte = 0
einf_zeichen = 1


north = np.array([-1, 0])
south = np.array([1, 0])
east = np.array([0, 1])
west = np.array([0, -1])
neue_pos = np.array([])

gueltig_f_nordbewegung = ["J", "L", "|"]
gueltig_f_suedbewegung = ["F", "7", "|"]
gueltig_f_ostbewegung = ["-", "L", "F"]
gueltig_f_westbewegung = ["-", "J", "7"]

# Funktionen

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


def s_finden(irgendeinarry, suchzeichen):
    """
    Suchzeichen finden und Position im Array zurückgeben
    """
    zeilen_nr = 0
    for zeile in irgendeinarry:
#        print(zeilen_nr, ":", zeile)
        if suchzeichen in zeile:
            fund_spalte = zeile.index(suchzeichen)
            fund_zeile = zeilen_nr
        zeilen_nr += 1

    return fund_zeile, fund_spalte


def next_step(akt_pos, last_pos):
    """
    ermittelt in Abhängigkeit des Zeichens undd des Vorgängers die nächste Position im Rohsystem
    """
    new_pos = np.array([])
    
#    print("aktuelle Position", akt_pos, document[akt_pos[0]][akt_pos[1]])
    zeichen = document[akt_pos[0]][akt_pos[1]]
    if zeichen == "S":
        if "bsp" in file:
            zeichen = "F"   # hier muss ich nachher noch Pfuschen und aus dem Text raussuchen 
        else:
            zeichen = "7"
    
    if zeichen in gueltig_f_nordbewegung:
        if not np.array_equal(akt_pos + north, last_pos):
            new_pos = akt_pos + north
#            print(zeichen, "ist gueltig für Nordbewegung")

    if zeichen in gueltig_f_ostbewegung:
        if not np.array_equal(akt_pos + east, last_pos):
            new_pos = akt_pos + east  
#            print(zeichen, "ist gueltig für Ostbewegung") 
        
    if zeichen in gueltig_f_suedbewegung:
        if not np.array_equal(akt_pos + south, last_pos):
            new_pos = akt_pos + south
#            print(zeichen, "ist gueltig für Suedbewegung")
            
    if zeichen in gueltig_f_westbewegung:
        if not np.array_equal(akt_pos + west, last_pos):
            new_pos = akt_pos + west
#            print(zeichen, "ist gueltig für Westbewegung")

#    print("new pos", new_pos)
    
    return new_pos


def leere_matrix_aus_matrix_erzeugen(matrix):
    """
    erzeugt eine gleichgroße Matrix mit . für jeden Buchstaben in der originalmatrix
    """
    new_matrix = []
    for line in matrix:
        new_matrix_line = []
        for buchstabe in line:
            new_matrix_line.append(0)
        new_matrix.append(new_matrix_line)
    
    return new_matrix


def print_field(matrix):
    # danke an
    # https://plainenglish.io/blog/a-python-example-of-the-flood-fill-algorithm-bced7f96f569
    # this function will print the contents of the array
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
        # value by column and row
            print(matrix[y][x], end=' ')
            if x == len(matrix[0])-1:
                # print a new line at the end of each row
                #print('\n')
                print(" ")

def zeichen_ersetzen(matrix, zeile, spalte, einf_zeichen):
    """
    ersetzt das bestehende Zeichen der document2 matrix durch einen Stern
    """
    matrix[zeile].pop(spalte)
    matrix[zeile].insert(spalte, einf_zeichen)
                

def flood_fill(matrix, x, y, target, replacement):
    """
    Quelle: https://plainenglish.io/blog/a-python-example-of-the-flood-fill-algorithm-bced7f96f569
    """
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != target:
        return
    matrix[x][y] = replacement
    flood_fill(matrix, x + 1, y, target, replacement)
    flood_fill(matrix, x - 1, y, target, replacement)
    flood_fill(matrix, x, y + 1, target, replacement)
    flood_fill(matrix, x, y - 1, target, replacement)

def berechne_inhalt(matrix):
    # Dupliziere die Matrix, um sie zu modifizieren
    mod_matrix = [row[:] for row in matrix]

    # Wende Flood Fill vom Rand der Matrix aus an
    for i in range(len(mod_matrix)):
        for j in [0, len(mod_matrix[0]) - 1]:
            flood_fill(mod_matrix, i, j, 0, 9)
    for j in range(len(mod_matrix[0])):
        for i in [0, len(mod_matrix) - 1]:
            flood_fill(mod_matrix, i, j, 0, 9)
    
    print_field(mod_matrix)
    print(" ")

    # Zähle die unmarkierten Zellen, die den Inhalt darstellen
    return sum(row.count(0) for row in mod_matrix)
        
        
        

# Ausführung der Funktionen

# Datei einlesen und ausgeben
document = einlesen(file)
zeilen_no = 0
for zeile in document:
    print(zeilen_no, ":", zeile)
    zeilen_no +=1
print(" ")

document2 = leere_matrix_aus_matrix_erzeugen(document)

# Das "S" suchen und die Position zurückgeben
find = s_finden(document, suchzeichen)
fund_zeile = find[0]
fund_spalte = find[1]

print("Gefunden:", document[fund_zeile][fund_spalte], "in Zeile", fund_zeile, "Spalte", fund_spalte)  
print(" ")

akt_pos = np.array([fund_zeile, fund_spalte])

while rundlauf < 1:
    neue_pos = next_step(akt_pos, last_pos)
    zeichen_ersetzen(document2, akt_pos[0], akt_pos[1], einf_zeichen) ###
#    print(neue_pos)
#    print("Nächste Position", neue_pos, document[neue_pos[0]][neue_pos[1]])
    last_pos = akt_pos
    akt_pos = neue_pos
    schritte +=1
    if document[neue_pos[0]][neue_pos[1]] == "S":
        rundlauf += 1

print("Anzahl Schritte:", schritte)
print("Lösungsantwort: ", schritte/2)
print(" ")

zeilen_no = 0
for zeile in document2:
    print(zeilen_no, ":", zeile)
    zeilen_no +=1
print(" ")


print_field(document)
print(" ")
print_field(document2)
print(" ")

inhalt = berechne_inhalt(document2)
print("Inhalt des Pfades:", inhalt)
