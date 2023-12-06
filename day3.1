file = "AOC_day3_input_bsp.txt"
document = []
org_matrix = []

def einlesen(filename):
    """
    liest alle Zeilen eines Textfiles ein und speichert jede einzelne Zeile in einer Liste
    """
    with open(filename, "r") as file:
        # read file line by line and output the lines
        for line in file:
            line = line.strip()
            new_string = ""
            
            m_zeile = []
            
            for zeichen in line:
                if zeichen == ".":
                    m_zeile.append("")
                elif zeichen.isdigit():
                    m_zeile.append(zeichen) #hier hatte ich vorher int(zeichen) stehen
                else:
                    m_zeile.append("x")  
                
            document.append(m_zeile)
    return document


def leere_matrix_erzeugen(zeilen, spalten):
    """
    erzeugt eine leere Matrix in derselben Größe wie Originalmatrix
    """
    new_matrix = []
    elemente = []
    value = 0
    
    for i in range(0, zeilen):
        elemente = []
        for j in range(0, spalten):
           elemente.append(value) 
        new_matrix.append(elemente)
        
    return new_matrix

# Einlesen und Ausgabe der Originalmatrix
org_matrix = einlesen(file)
for l in range(len(org_matrix)):
    print(org_matrix[l])

# Erzeugen der Gut_Matrix, zuerst als leere Matrix
zeilen = len(org_matrix)  #ermittelt die Anzahl Zeilen
spalten = len(org_matrix[0])  #ermittelt die Anzahl Spalten = länge des jeweiligens Strings
print("Zeilen: ", zeilen, "Spalten: ", spalten)

gute_matrix = leere_matrix_erzeugen(zeilen, spalten)


a = 0
b = 0
such_zeichen = "x"

for zeile in org_matrix:
    b = 0
    for zeichen in zeile:
        if zeichen == such_zeichen:
            # links und rechts daneben
            gute_matrix[a][b+1] = 1
            gute_matrix[a][b-1] = 1
            # oben und unten drunter (je 3 stück)
            gute_matrix[a+1][b+1] = 1
            gute_matrix[a+1][b] = 1
            gute_matrix[a+1][b-1] = 1
            gute_matrix[a-1][b+1] = 1
            gute_matrix[a-1][b] = 1
            gute_matrix[a-1][b-1] = 1
        b = b + 1
    #        print("x ist auf Pos: ", zeile.index(such_zeichen))
    #    else:
    #        print("kein x enthalten")
    a = a + 1

print("Gute Matrix")
for l in range(len(gute_matrix)):
    print(gute_matrix[l])

b = 0
zw_matrix = [] 

print("Zwischenergebnis Matrix")
for zeile in org_matrix:
    c = 0
    elemente = []
    for zeichen in zeile:
        if zeichen.isdigit() and gute_matrix[b][c] == 1:
            elemente.append(zeichen)
        else:
            elemente.append(" ")
        c = c + 1
    zw_matrix.append(elemente)
    b = b + 1
            
#print("Zwischen Matrix")
#for l in range(len(zw_matrix)):
#    print(zw_matrix[l])

for _ in range(10):
    done = 0
    b = 0
    for zeile in zw_matrix:
        c = 0
        for zeichen in zeile:
            if c-1 >= 0:
                if zeichen.isdigit() and org_matrix[b][c-1].isdigit():
#                    print("wert 1 links: ", org_matrix[b][c-1])
                    zeile.pop(c-1)
                    zeile.insert(c-1, org_matrix[b][c-1])
                    done = 1
            if c+1 < len(org_matrix[b]):
                if zeichen.isdigit() and org_matrix[b][c+1].isdigit():
#                    print("wert 1 rechts: ", org_matrix[b][c+1])
                    zeile.pop(c+1)
                    zeile.insert(c+1, org_matrix[b][c+1])
                    done = 1
            c = c + 1
        b = b + 1        

print("Zwischen Matrix 2")
for l in range(len(zw_matrix)):
    print(zw_matrix[l])

#print("Lösungsmatrix")
#for l in range(len(loesungs_matrix)):
#    print(loesungs_matrix[l])

t_string = ""
z_string = ""

for zeile in zw_matrix:
    for item in zeile:
        t_string = t_string + item
#    t_string = t_string + z_string
t_string = t_string.split(" ")
print(t_string)

loesungs_matrix = []
for item in t_string:
    elemente = []
    if item.isdigit():
        loesungs_matrix.append(int(item))
    else:
        loesungs_matrix.append(0)
    
print(loesungs_matrix)
summe = sum(loesungs_matrix)

print("Die gesuchte Gesamtsumme ist", summe)
