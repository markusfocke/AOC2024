## Teil 1
## successful

import time


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

def print_field(matrix):
    """
    https://plainenglish.io/blog/a-python-example-of-the-flood-fill-algorithm-bced7f96f569
    this function will print the contents of the array
    """
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
        # value by column and row
            print(matrix[y][x], end=' ')
            if x == len(matrix[0])-1:
                print(" ")


def find_s_in_list(matrix, suchzeichen):
    """sucht das S in der gegebenen Matrix"""
    rows = 0
    for line in matrix:
        if suchzeichen in line:
            col = line.index("S")
            row = rows
            break
        rows += 1
    
    return row, col
            
def array_size(matrix):
    """ermittelt die Größe einer Matrix-Liste"""
    rows = len(matrix)
    cols = len(matrix[0])
    
    return rows, cols

def walk(current_pos, direction, distance):
    """
    ermittelt die nächste Position ausgehend von einer current_position
    """
    directions = {"L": (0, -1), "R": (0, 1), "U": (1, 0), "D": (-1, 0)}
    d = direction
    dist = distance
    dr, dc = directions[d]
    
    new_pos = (current_pos[0] + dr * dist, current_pos[1] + dc * dist)   #dr delta row, dc delta cols
    
    return new_pos
    

def walk_all_dirs(current_pos):
    """gehe von deiner aktuellen Position einen Schritt nach oben, unten, links rechts
    """
    dir_list = ("L", "R", "U", "D")
    new_pos = current_pos
    distance = 1
    step_psbl = False
    zeichen = "."  #keine gute Art, das Zeichen hier hin zu schreiben, aber egal
    
    for direction in dir_list:
            new_pos = walk(current_pos, direction, distance)

            step_psbl = rocks_or_plots(new_pos, zeichen)
            if step_psbl == True:
                rrow, ccol = current_pos
                zeile = document[rrow]
                neue_zeile = zeile[:ccol] + "." + zeile[ccol + 1:]
                document[rrow] = neue_zeile
            
            
def rocks_or_plots(pos, zeichen):
    """
    ermittelt, ob an der neuen stelle ein Rock "#" oder ein Plot "."" ist
    fügt an der stelle ein "O" ein, wenn True
    """
    row, col = pos
    neues_zeichen = "O"
    nps = []
    
    if row >= 0 and row < rows and col >= 0 and col < cols:    
        if document[row][col] == zeichen or document[row][col] == "O":
            zeile = document[row]
            neue_zeile = zeile[:col] + neues_zeichen + zeile[col + 1:]
            document[row] = neue_zeile
            nps = [row, col]
            print("nexter schritt", nps)
            
            if nps not in new_positions:
                new_positions.append(nps)
            return True
    
    return False
        
def count_garden_plots(matrix, zeichen):
    total_plots = 0
    
    for line in matrix:
        total_plots += line.count(zeichen)
        
    return total_plots        

def time_taking(anzahl_cycles, max_cycles):
    """ermittelt die Zeitdifferenz und gibt die Hochrechnung aus"""
    duration = end_time - start_time
    print(f"Laufzeit des Codes: {end_time - start_time} Sekunden")
    print("Schätzung Laufzeit für", max_cycles, "Cycles:", duration * max_cycles/anzahl_cycles/60/60, "h")
        
        
        

file = "AOC_day21_input_bsp.txt"
document = []
cur_positions = []

document = einlesen(file)
print_field(document)

rows, cols = array_size(document)
print("die Matrix hat", rows, "x", cols, "cols" )

current_position = find_s_in_list(document, "S")
row, col = current_position
print("das S ist in row", row, "col", col)

# Startelement in O wandeln und position in Liste speichern
rocks_or_plots(current_position, "S")
cur_positions.append(current_position)


print("cur positions", cur_positions)

i = 0
max_steps = 6

# Zeitmessung Start
start_time = time.time()  


for steps in range(max_steps):
    print("Schritt: ", steps)
    print(cur_positions)
    new_positions = []

    for item in cur_positions:
        if item[0] >= 0 and item[0] < rows and item[1] >= 0 and item[1] < cols:
            walk_all_dirs(item)

    cur_positions = new_positions.copy()
    print_field(document)


# Zeitmessung Ende            
end_time = time.time()


print(cur_positions)
#print_field(document)

total_plots = count_garden_plots(document, "O")

print("  ")
time_taking(max_steps, 64)
print("  ")
print("The elf can reach", total_plots, "garden plots in", max_steps,"steps")
print("  ")



    

