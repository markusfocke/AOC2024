# Day9, Teil 2, successful

file = "AOC_day9_input.txt"
document = []
values = []
oasis_liste = []

def einlesen(filename):
    """
    liest alle Zeilen eines Textfiles ein und speichert jede einzelne Zeile in einer Liste
    """
    with open(filename, "r") as file:
        # read file line by line and output the lines
        for line in file:
            line = line.strip()
            zeile =line.split(" ")
            values = []
            for item in zeile:
                wert = int(item)
                values.append(wert)
            document.append(values)
    return document


oasis_liste = einlesen(file)
for line in oasis_liste:
    print(line)
print(" ")

#  ab hier die weitere Bearbeitung

total_prognose_werte = 0
pv_liste = []


for zeile in oasis_liste:
    ableitungs_liste = [1, 1]
    diff_liste = []
    ableitung = 1
    prognose_wert = 0
    nullen_zaehler = 1
    
    while nullen_zaehler > 0:      # ursprünglich mit sum(ableitungs_liste) != 0  
        ableitungs_liste = np.diff(zeile, ableitung)
        zeilensumme = sum(ableitungs_liste)
        print("zeile", zeile, "Ableitung", ableitung, ableitungs_liste)
        ableitung +=1
        diff_liste.append(ableitungs_liste[0])
        
        nullen_zaehler = 0
        for zahl in ableitungs_liste:
            if zahl != 0:
                nullen_zaehler += 1
        
    print(diff_liste)
    
    abzugswert = 0
    for i in range(len(diff_liste)):
        if i % 2 == 0:
            abzugswert = abzugswert - diff_liste[i]
        else:
            abzugswert = abzugswert + diff_liste[i]
    print("Abzugswert", abzugswert)
    
    prognose_wert = zeile[0] + abzugswert
    
    
    
    print("Vorgehender prognostizierter Wert:", prognose_wert)
    print(" ")
    pv_liste.append(prognose_wert)
    total_prognose_werte = total_prognose_werte + prognose_wert

print("liste mit allen Prognosewerten: ", pv_liste, "summe aller Werte: ", sum(pv_liste))
print("Die Summe aller prognostizierten Werte beträgt: ", total_prognose_werte)
