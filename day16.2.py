# Teil 2
# Finally SUCCESSFUL!!!

file = "AOC_day16_input.txt"
document = []
directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}


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
                
def matrix_in_datei_schreiben(matrix, dateiname):
    """
    Schreibt die Matrix in eine Textdatei
    """
    with open(dateiname, "w") as file:
        for zeile in matrix:
            file.write(' '.join(zeile) + '\n')


def merge_matrices(input_matrix, output_matrix):
    """ Führt die # aus der output_matrix mit der input_matrix zusammen und gibt eine dritte Matrix aus. """
    merged_matrix = []

    for y in range(len(output_matrix)):
        # Konvertiere die Zeile der input_matrix in eine Liste von Zeichen
        input_row_list = list(input_matrix[y])

        for x in range(len(output_matrix[0])):
            if output_matrix[y][x] == "#" and input_matrix[y][x] == ".":
                input_row_list[x] = "#"

        # Konvertiere die modifizierte Zeilenliste zurück in einen String
        merged_matrix.append(''.join(input_row_list))

    return merged_matrix

                
def matrix_copy(matrix):
    new_line = ""
    new_matrix = []
    
    for line in matrix:
        new_line = "."*len(line)
        new_matrix.append(new_line)        
    return new_matrix

def array_size(matrix):
    """ermittelt die Größe einer Matrix-Liste"""
    rows = len(matrix)
    cols = len(matrix[0])
    
    return rows, cols

def walk(current_pos, direction):
    """
    ermittelt die nächste Position ausgehend von einer current_position
    """   
    d = direction
    dist = 1
    dr, dc = directions[d]
    new_pos = (current_pos[0] + dr * dist, current_pos[1] + dc * dist)   #dr delta row, dc delta cols
    
    return new_pos

def energize(pos):
    """schreibt "#" an die position im ergebnisdokument"""
    string_zeile = ""
    row, col = pos
    string_zeile = erg_document[row][:col] + "#" + erg_document[row][col + 1:]
    erg_document[row] = string_zeile

    
def count_energized_tiles(matrix):
    t_val = 0
    for line in matrix:
        l_val = line.count("#")
        t_val = t_val + l_val
    
    return t_val

def beam_splitten(pos, vektor):
    
    if pos in pos_liste and dir_liste[pos_liste.index(pos)] == vektor:
        hdj = 1
    else:
        pos_liste.append(pos)    #aktuelle position in die pos_liste eintragn
        dir_liste.append(vektor) #zugehörigen vektor in die Ricthungsliste eintragen
        

def get_next_direction(pos, direction):
    
    row, col = pos
    # zeichen gibt an, was der Beam antrifft
    zeichen = document[row][col]
#    print("Zeichen gefunden", zeichen, "an Feld", pos)
    vektor = direction
        
    if direction == "R":
        if zeichen == "/":
            vektor = "U"
        elif zeichen == "\\":
            vektor = "D"
        elif zeichen == "|":
            vektor = "D" #vektor für den neuen Beam
            beam_splitten(pos, vektor)
            vektor = "U" #vektor für den "alten" beam
            
    elif direction == "L":         
        if zeichen == "/":
            vektor = "D"
        elif zeichen == "\\":
            vektor = "U"
        elif zeichen == "|":
            vektor = "D"
            beam_splitten(pos, vektor)
            vektor = "U" #vektor für den "alten" beam
    
    elif direction == "D":
        if zeichen == "/":
            vektor = "L"
        elif zeichen == "\\":
            vektor = "R"
        elif zeichen == "-":
            vektor = "R"
            beam_splitten(pos, vektor)
            vektor = "L" #vektor für den "alten" beam

    elif direction == "U":
        if zeichen == "/":
            vektor = "R"
        elif zeichen == "\\":
            vektor = "L"
        elif zeichen == "-":
            vektor = "R"
            beam_splitten(pos, vektor)
            vektor = "L" #vektor für den "alten" beam
            
    new_direction = vektor
    
    return new_direction

def main_loop(start_pos, start_dir):

    i = 0 
    ze_count = 0
    en_tiles = 0

    for item in pos_liste:
        # beide listen lesen für den nächsten Beam
        row, col = item
        pos = item
        drx = dir_liste[i]
        ze = 0

        while True:

    #            if ze%10 == 0:
    #                print("Cycle", i, "Pos", item, "durchlauf", ze)
    #            print("pos", pos, "row", row, "col", col, "dir", drx)
                energize(pos)  # im Ergebnisdokument die alte Position markieren

                n_drx = get_next_direction(pos, drx)   #ermittle mir zur position die Richtung
    #            print("new direction", n_drx)
                n_pos = walk(pos, n_drx) # gehe in diese Richtung
    #            print("new position after walk", n_pos)

                # position und richtung auf die neuen Werte setzen
                drx = n_drx
                pos = n_pos
                row, col = pos

                ze +=1

                if row < 0 or row >= max_rows or col < 0 or col >= max_cols:
    #                print("Und raus aus der Matrix für", item)
    #                print(" ")
                    break

                # print("pos", pos, "row", row, "col", col, "dir", drx)
                energize(pos)  # im Ergebnisdokument die neue Position markieren

                if ze > abbruch_cycles:
                    ze_count += 1
                    print("-->", abbruch_cycles, "erreicht")
                    break

        i += 1
        if i > abbruch_cycles:
            print("--> ABBRUCH", abbruch_cycles, "erreicht")
            break
    
    en_tiles = count_energized_tiles(erg_document)
    print(" ")        
    print("Energized Tiles:", en_tiles)
    print("anzahl abbrüche innere Schleife", ze_count)
    return en_tiles, ze_count

####

einlesen(file)

max_rows, max_cols = array_size(document)
print("Die Ursprungsmatrix ist", max_rows, "x", max_cols, "groß")
print(" ")
#print("Vorgabe")
#print_field(document)  

erg_document = matrix_copy(document)

abbruch_cycles = 10000
max_energ_tiles = 0
mmax_tiles = 0

start_position = [0, 0]
start_direction = "R"

for rr in range(max_rows):
    start_position = [rr, 0]
    pos_liste = []
    dir_liste = []
    pos_liste.append(start_position)
    dir_liste.append(start_direction)

    energ_tiles, inner_abbr = main_loop(start_position, start_direction)
    print("Number of energized tiles with start pos", start_position, start_direction, inner_abbr, ":", energ_tiles)
    if energ_tiles > max_energ_tiles:
        max_energ_tiles = energ_tiles
    erg_document = matrix_copy(document)
print(" ")
print("maximale Anzahle energized tiles", max_energ_tiles)
if max_energ_tiles > mmax_tiles:
    mmax_tiles = max_energ_tiles



start_position = [0, max_cols-1]
start_direction = "L"

for rr in range(max_rows):
    start_position = [rr, max_rows-1]
    pos_liste = []
    dir_liste = []
    pos_liste.append(start_position)
    dir_liste.append(start_direction)

    energ_tiles, inner_abbr = main_loop(start_position, start_direction)
    print("Number of energized tiles with start pos", start_position, start_direction, inner_abbr, ":", energ_tiles)
    if energ_tiles > max_energ_tiles:
        max_energ_tiles = energ_tiles
    erg_document = matrix_copy(document)
print(" ")
print("maximale Anzahle energized tiles", max_energ_tiles)
if max_energ_tiles > mmax_tiles:
    mmax_tiles = max_energ_tiles

    
start_position = [0, 0]
start_direction = "D"

for cc in range(max_cols):
    start_position = [0, cc]
    pos_liste = []
    dir_liste = []
    pos_liste.append(start_position)
    dir_liste.append(start_direction)

    energ_tiles, inner_abbr = main_loop(start_position, start_direction)
    print("Number of energized tiles with start pos", start_position, start_direction, inner_abbr, ":", energ_tiles)
    if energ_tiles > max_energ_tiles:
        max_energ_tiles = energ_tiles
    erg_document = matrix_copy(document)
print(" ")
print("maximale Anzahle energized tiles", max_energ_tiles)
if max_energ_tiles > mmax_tiles:
    mmax_tiles = max_energ_tiles

    
start_position = [max_rows-1, 0]
start_direction = "U"

for cc in range(max_cols):
    start_position = [max_rows-1, cc]
    pos_liste = []
    dir_liste = []
    pos_liste.append(start_position)
    dir_liste.append(start_direction)

    energ_tiles, inner_abbr = main_loop(start_position, start_direction)
    print("Number of energized tiles with start pos", start_position, start_direction, inner_abbr, ":", energ_tiles)
    if energ_tiles > max_energ_tiles:
        max_energ_tiles = energ_tiles
    erg_document = matrix_copy(document)
print(" ")
print("maximale Anzahle energized tiles", max_energ_tiles)
if max_energ_tiles > mmax_tiles:
    mmax_tiles = max_energ_tiles
    

print("TOTAL ENERGIZABLE TILES", mmax_tiles)



#print("Kontrollmatrix")
#kontroll_matrix = merge_matrices(document, erg_document)
#print_field(kontroll_matrix)

#matrix_in_datei_schreiben(erg_document, "AOC_day16_output.txt")
#matrix_in_datei_schreiben(kontroll_matrix, "AOC_day16_kontroll_matrix.txt")
