# Teil 1, große liste

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

def matrix_in_datei_schreiben(matrix, dateiname):
    """
    Schreibt die Matrix in eine Textdatei
    """
    with open(dateiname, "w") as file:
        for zeile in matrix:
            file.write(' '.join(zeile) + '\n')
            

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
                
                
def leere_matrix_erzeugen(spalten, zeilen):
    """
    erzeugt eine Matrix mit . für jeden Buchstaben 
    """
    new_matrix = []
    for i in range(zeilen):
        new_matrix.append("."*spalten)
    
    return new_matrix

def leeres_array_erzeugen(spalten, zeilen):
    new_array = np.full((spalten, zeilen), '.')
    
    return new_array

def flood_fill(x ,y, old, new):
    """
    Quelle: https://plainenglish.io/blog/a-python-example-of-the-flood-fill-algorithm-bced7f96f569
    """
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix):
        return
    # secondly, check if the current position equals the old value
    if matrix[y][x] != old:
        return

    # thirdly, set the current position to the new value
    matrix[y][x] = new
    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)
    
    
def flood_fill_iterativ(x, y, old, new):
    if matrix[y][x] != old:
        return

    # Eine Warteschlange (Queue) verwenden, um zu speichernde Positionen zu verwalten
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)

        if matrix[y][x] != old:
            continue

        # Aktuelle Position auf den neuen Wert setzen
        matrix[y][x] = new

        # Nachbarn überprüfen und zur Warteschlange hinzufügen
        if x > 0 and matrix[y][x-1] == old:
            queue.append((x-1, y))
        if x < len(matrix[0])-1 and matrix[y][x+1] == old:
            queue.append((x+1, y))
        if y > 0 and matrix[y-1][x] == old:
            queue.append((x, y-1))
        if y < len(matrix)-1 and matrix[y+1][x] == old:
            queue.append((x, y+1))
    


def baggern(startpos, schritte, richtung):
    """
    läuft schritte in richtung von einer startposition + 1 aus
    """
    
    end_pos = []
    k = 0
    l = 0
    
    for i in range(1, schritte +1):
        
        if richtung == "R":
            k = startpos[0]
            l = startpos[1] + i
        elif richtung == "L":
            k = startpos[0]
            l = startpos[1] - i
        elif richtung == "D":
            k = startpos[0] + i
            l = startpos[1]
        elif richtung == "U":
            k = startpos[0] - i
            l = startpos[1]
        
        matrix[k][l] = "#"
    
    end_pos = [k, l]    
    return end_pos


einlesen(file)
#print(document)

spalten = 500
zeilen = 500

#matrix = leere_matrix_erzeugen(spalten, zeilen)
#print_field(matrix)

matrix = leeres_array_erzeugen(spalten, zeilen)

# teilen der Baggerbewegungsliste
baggerbewegungen = []
for line in document:
    line2 = line.split(" (")
    baggerbew = line2[0].split(" ")
    baggerbewegungen.append(baggerbew)
    
print(baggerbewegungen)

start_pos = [400, 200]

for zeile in baggerbewegungen:
    end_pos = baggern(start_pos, int(zeile[1]), zeile[0])
    start_pos = end_pos

#print_field(matrix)

flood_fill_iterativ(125, 250, ".", "#")
#flood_fill(1, 1, ".", "#")
print("Doing flood fill")

#print_field(matrix)
#print(matrix)



print("Anzahl # in der Matrix:", np.count_nonzero(matrix == "#"))

matrix_in_datei_schreiben(matrix, "AOC_day18_output.txt")
