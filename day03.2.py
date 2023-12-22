# Teil 2
# Try 1: 32965120 too low
# Hypothese 1: wenn zwei gleiche Zahlen um einen Stern herum stehen, wird die zweite Zahl nicht hinzugefügt
# Hypothese korrekt, hilft aber nicht. kommt nämlich nicht vor
# Hypthese 2: Es wird immer nur der erste Stern pro Zeile gesucht --> korrekt! Suchfunktion geändert
# SUCCESS

file = "AOC_day3_input.txt"
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
                          
def print_field(matrix):
    # danke an
    # https://plainenglish.io/blog/a-python-example-of-the-flood-fill-algorithm-bced7f96f569
    # this function will print the contents of the array
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
        # value by column and row
            print(matrix[y][x], end=' ')
            if x == len(matrix[0])-1:
                print(" ")
                           
            
def find_s_in_list(matrix):
    """sucht das S in der gegebenen Matrix"""
    rows = 0
    suchzeichen = "*"
    zeichen_liste = [] 
    for line in matrix:
        if suchzeichen in line:
            for zeichen in range(len(line)):
                col = 0
                if line[zeichen] == "*":
                    col = zeichen
                    #col = line.index("*")
                    row = rows
                    pos = [row, col]
                    zeichen_liste.append(pos)
        rows += 1
    
    return zeichen_liste

def array_size(matrix):
    """ermittelt die Größe einer Matrix-Liste"""
    rows = len(matrix)
    cols = len(matrix[0])
    
    return rows, cols

def walk(current_pos, direction, distance):
    """
    ermittelt die nächste Position ausgehend von einer current_position
    """
    directions = {"L": (0, -1), 
                  "R": (0, 1), 
                  "U": (1, 0), 
                  "D": (-1, 0),
                  "UR": (1, 1),
                  "UL": (1, -1),
                  "DR": (-1, 1),
                  "DL": (-1, -1)}
    d = direction
    dist = distance
    dr, dc = directions[d]
    
    new_pos = (current_pos[0] + dr * dist, current_pos[1] + dc * dist)   #dr delta row, dc delta cols
    
    return new_pos
    

def walk_all_dirs(current_pos):
    """gehe von deiner aktuellen Position einen Schritt nach oben, unten, links rechts
    """
    dir_list = ("L", "R", "U", "D", "UL", "UR", "DL", "DR")
    new_pos = current_pos
    distance = 1
    
    for direction in dir_list:
            number = 0
            no = []
            new_pos = walk(current_pos, direction, distance)
            ### jetzt schauen, ob an den new_pos jeweils eine Ziffer ist und wenn, dann ganze Zahl mit adjacent no ermitteln
            row, col = new_pos
            if document[row][col].isdigit():
                no = adjacent_number(document[row], col)
                number = int(no[0])
                pos_no = int(no[1])
                no = [number, pos_no]
                # hier noch ändern, schon drin ist nicht gut bei zwei gleichen Zahlen
                
                if no not in number_list:
                    number_list.append(no)


            print(new_pos, number, no)
            

def adjacent_number(string, col):
    """
    ermittelt in einem String ob an der Position eine Zahl ist und gibt diese vollständig zurück
    achtung, wenn keine ziffer gibt die Funktion leer zurück
    """
    new_string = ""
    if string[col].isdigit():
        new_string = string[col]
        i = col - 1
        l = col
        while string[i].isdigit():
            new_string = string[i] + new_string
            l = i
            i -= 1

        j = col + 1
        while j < len(string) and string[j].isdigit():
            new_string = new_string + string[j]
            j +=1

            
    return new_string, l



einlesen(file)
max_rows, max_cols = array_size(document)
print("Die Matrix ist", max_rows, "x", max_cols)
print_field(document)
print(" ")

sternliste = find_s_in_list(document)
print("liste mit sternen", sternliste)
t_gear_ratio = 0

for item in sternliste:
    number_list = []
    gear_ratio = 0
    row, col = item
    walk_all_dirs(item)
    print("no list", number_list)
    if len(number_list) == 2:
        gear_ratio = number_list[0][0] * number_list[1][0]
    t_gear_ratio += gear_ratio

print(t_gear_ratio)

    ### 
    #walk um den stern herum
    #zu jedem schritt adjacent_number ermitteln und in liste speichern, wenn number noch nicht enthalten
    
