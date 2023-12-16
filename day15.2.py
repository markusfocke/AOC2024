# Teil 2, real world

file = "AOC_day15_input.txt"
document = []


def einlesen(filename):
    """
    liest alle durch Komma getrennten Einheiten eines Textfiles ein und speichert jede einzelne in einer Liste
    """
    with open(filename, "r") as file:
        data = file.read()
        lines = data.strip().split(",")  # Kommaseparation
        for line in lines:
            document.append(line)
    return document
                          


def curr_val_calc(string):
    """
    berechnung des Werts nach dem HASH Algo
    """
    string_vals = []
    string_vals = list(string.encode('ascii'))   # erzeugt eine Liste der ASCII Werte des Inputstrings
    
    current_value = 0
    for value in string_vals:
            current_value = current_value + value
            current_value = current_value * 17
            current_value = current_value % 256
    
    return current_value


# File einlesen
einlesen(file)

#erstellen eines leeren Dictionarys für die Boxen
boxes = {}
for i in range(256):
    boxes[i] = []
    
    
for item in document:
    print("after", item)
    insert = False 
    
    if "=" in item:
        lense = item.split("=")
        box_no = curr_val_calc(lense[0])  # gibt den Key der Box zurück

#        print(lense[0], ",", lense[1], "Box", box_no) 

#        print("inhalt von boxes box_no", boxes[box_no], lense[0])
        
        for count, element in enumerate(boxes[box_no]):
            if element[0] == lense[0]:
                    print("Bäm", count)
                    boxes[box_no].pop(count)
                    boxes[box_no].insert(count, lense)
                    insert = True
        
        if insert == False:
            boxes[box_no].append(lense)
            
            
    
        
    elif "-" in item:
        
        lense = item.replace("-", "")    # das hier ist "qp" oder so
        box_no = curr_val_calc(lense)    # das hier ist die Box Nummer 
        print(lense, "Box", box_no)
        
        for count, element in enumerate(boxes[box_no]):
            if element[0] == lense:
                    print("Delete", count)
                    boxes[box_no].pop(count)

    
    print("Box", boxes[0])
    print("Box", boxes[1])
    print("Box", boxes[3])
    print(" ")
            
        
        

# print(boxes)

def focussing_power(dictionary):
    
    total_f_power = 0
    lense_f_power = 0
    
    for line in dictionary:
#        print(line, dictionary[line])
        for slot, element in enumerate(dictionary[line]):
            
            ###
            multiplier1 = curr_val_calc(element[0]) + 1
            multiplier2 = slot + 1
            multiplier3 = int(element[1])
            lense_f_power = multiplier1 * multiplier2 * multiplier3
            
            print(element[0], ":", multiplier1, 
                  "(box", curr_val_calc(element[0]), 
                  ") * ", "slot no", multiplier2, 
                  "* focal length", multiplier3, 
                  "=", lense_f_power)
            total_f_power = total_f_power + lense_f_power
            
    return total_f_power
        

print("So, the above example ends up with a total focusing power of", focussing_power(boxes))

