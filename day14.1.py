import time

file = "AOC_day14_input.txt"
document = []
document2 = []
new_doc = []
new_doc2 = []
new_doc3 = []


def einlesen(filename):
    """
    liest alle Zeilen eines Textfiles ein und speichert jede einzelne Zeile in einer Liste
    """
    with open(filename, "r") as file:
        # read file line by line and output the lines
        for line in file:
            line = line.strip()
            items = []
            for zeichen in line:
                items.append(zeichen)
            document.append(items)
    return document

def print_field(matrix):
    """ 
    danke an https://plainenglish.io/blog/a-python-example-of-the-flood-fill-algorithm-bced7f96f569
    this function will print the contents of the array
    """
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
        # value by column and row
            print(matrix[y][x], end=' ')
            if x == len(matrix[0])-1:
                # print a new line at the end of each row
                #print('\n')
                print(" ")
           
        
def steine_rollen(matrix):
    """
    laesst alle runden steine bis zum anfang der Zeile oder bis zum # rollen
    """
    for zeile in range(len(matrix)):

        item_pos = 0
        einf_pos = 0

        for item in matrix[zeile]:
            if item == "O":
                matrix[zeile][item_pos] = "."
                matrix[zeile][einf_pos] = "O"
                einf_pos = einf_pos +1

            elif item == "#":
                einf_pos = item_pos +1

            item_pos += 1
    
    return matrix


def matrix_kippen(in_document):
    """
    kippt eine Matrix um 90 grad gegen den Uhrzeigersinn und gibt neue Matrix zurück
    """
    t_document = []
    breite = len(in_document[0])-1

    for spalte in range(breite, -1 ,-1):
        t_zeile = []
        for zeile in in_document:
            t_zeile.append(zeile[spalte])
        t_document.append(t_zeile)
    
    return t_document


def matrix_zurueck_kippen(in_document):
    """
    kippt eingangsmatrix um 90 Grad MIT dem UZS
    """
    n_document = matrix_kippen(matrix_kippen(matrix_kippen(in_document)))
    
    return n_document


def load_calculation(matrix):
    """
    berechnet die gewichtete Zeilensumme der Nullen
    """
    total_weight = 0
    weight = len(matrix)
    for line in matrix:
        rocks_line = line.count("O")
        line_weight = rocks_line * weight
        print(weight, ":", "anzahl:", rocks_line, "line weight", line_weight )
        weight = weight -1
        total_weight = total_weight + line_weight
    
    return total_weight


### hier beginnt der Ablaufcode                

document = einlesen(file)
org_document = document

print("Ausgangsmatrix")
print_field(org_document)
print(" ")

# Zeitmessung Start
start_time = time.time()  

# irgendwie wird document und org_document überschrieben, weiß aber nicht wieso

print("Gedrehte Matrix")
new_doc = matrix_kippen(document)
print_field(new_doc)
print(" ")

print("gerollte Steine")
new2_doc = steine_rollen(new_doc)
print_field(new2_doc)
print(" ")

print("zurückgedrehte Matrix")
new3_doc = matrix_zurueck_kippen(new2_doc)
print_field(new3_doc)
print(" ")

m_gewicht = load_calculation(new3_doc)
print("-------")
print("Gesamtgewicht der Matrix", m_gewicht)


# Zeitmessung Ende            
end_time = time.time()

duration = end_time - start_time

print(f"Laufzeit des Codes: {end_time - start_time} Sekunden")
