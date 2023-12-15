# successful

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
#            print("value", value, "current_value", current_value)
    
    return current_value


einlesen(file)
eintrags_val = 0
total_val = 0

#print(document)
for eintrag in document:
    eintrags_val = curr_val_calc(eintrag)
#    print("value", eintrag, "current_value", eintrags_val)
    total_val = total_val + eintrags_val 
    
print("Gesamt Wert: ", total_val)
