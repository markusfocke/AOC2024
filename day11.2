# Teil 2
# unsuccessfull


import numpy as np

file = "AOC_day11_input_bsp.txt"
document = []
document2 = []
koordinaten = []
such_zeichen = 0
weight_list = []



def einlesen(filename):
    """
    liest alle Zeilen eines Textfiles ein und speichert jede einzelne Zeile in einer Liste
    """
    
    with open(filename, "r") as file:
        # read file line by line and output the lines
        
        for line in file:
            line = line.strip()
            line2 = []
            line3 = []
            for buchstabe in line:
                line2.append(buchstabe)
                if buchstabe == "#":
                    line3.append(0)
                else:
                    line3.append(1)
                
            document.append(line2)
            document2.append(line3)

    return document, document2

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
    
def nullen_zeilen_verdoppeln(array):
    """
    Verdoppelt die Zeile mit nur Nullen
    gefunden in https://stackoverflow.com/questions/28663856/how-do-i-count-the-occurrence-of-a-certain-item-in-an-ndarray
    """
    zeilennr = 0
    num_zeros = 0
    i = 0
    e_columns = 2
    
    new_array = np.copy(array)
    rows, columns = new_array.shape
    
    input_zeile = np.full([1, columns], e_columns)
     
    for zeile in array:
        if np.all(zeile != 0):
            new_array = np.delete(new_array, zeilennr, axis = 0)            
            new_array = np.insert(new_array, zeilennr+i, input_zeile[0], axis=0)
        zeilennr +=1          
        
    return new_array


def nuller_zeilen_und_spalten_verdoppeln(array):
    """
    nutzt nullen zeilen verdoppeln, transponiert, zeilen again, wieder tranponieren
    """
    a1 = nullen_zeilen_verdoppeln(array)
    a2 = np.transpose(a1)
    a3 = nullen_zeilen_verdoppeln(a2)
    new_array = np.transpose(a3)
    
    return new_array                


def koordinaten_einlesen(in_array, such_zeichen):
    """
    findet alle Einsen im array und gibt die Koordinaten in Form zeile (zuerst) dann die spalte als matrix aus 
    """
    ones = np.array([])
    ones = np.where(in_array == such_zeichen)
    matrix1 = []

    i = 0

    for element in ones[0]:
        matrix1.append([ones[0][i], ones[1][i]]) 
        i +=1
    
    return matrix1


def gesamt_abstand(mat):
    """
    berechnet den x und y abstand aller koordinaten voneinander und bildet die summe der Beträge
    """
    total_dist = 0
    total_abstand = 0

    for element in mat:
        i = 0
        for i in range(len(mat)):
            distance = abs(element[0] - mat[i][0]) + abs(element[1] - mat[i][1])
#            print(element, element[0] - mat[i][0], element[1] - mat[i][1], distance)
            total_dist = total_dist + distance
    total_abstand = total_dist/2
    
    return total_abstand


def zeilen_spalten_summe(array, endpunkt):
    """
    berechnet die summe aller elemente in spalte und zeile bis zum angegebenen Punkt einschließlich
    liefert die zeilensumme, spaltensumme zurück
    """ 
    spaltenvektor = array[:endpunkt[0], endpunkt[1]]
    spaltensumme = spaltenvektor.sum()

    zeilenvektor = array[endpunkt[0], :endpunkt[1]+1]
    zeilensumme = zeilenvektor.sum() 
    
    return zeilensumme, spaltensumme


# This is where it all begins
#
# 

einlesen(file)
document3 = np.array(document2)
#print(document2)
print_field(document)
print(" ")
print_field(document3)
print(" ")

document4 = nuller_zeilen_und_spalten_verdoppeln(document3)
print_field(document4)
print(" ")

#n = np.count_nonzero(document4)
#n = document4[np.where(document4==0)]
n = document4.size - np.count_nonzero(document4)


knoten = n
kanten =  (n*(n-1))/2
print("Anzahl Knoten:", knoten, "Anzahl Kanten:", kanten)
print(" ")
koordinaten = koordinaten_einlesen(document4, such_zeichen)
print(koordinaten)
print(" ")

#print(gesamt_abstand(koordinaten))

for punkt in koordinaten:  #### [:2]
#    print(punkt)
    weight = zeilen_spalten_summe(document4, punkt)
#    print(weight)
    weight_list.append(weight) 

print(weight_list)
#print(np.array(weight_list))

print(gesamt_abstand(weight_list))
