# Teil 2, successful, Kudos an ceedee666 für so lange Tipps geben, bis ich nicht mehr nachdenken musste

import numpy as np

def kgv(a, b):
    return a * b // np.gcd(a, b)

def kgv_von_liste(zahlen):
    aktuelles_kgv = zahlen[0]
    for zahl in zahlen[1:]:
        aktuelles_kgv = kgv(aktuelles_kgv, zahl)
    return aktuelles_kgv



filename = "AOC_day8_input.txt"

with open(filename, "r") as file:
        data_text = file.read()
sections = data_text.split("\n\n")

weg = sections[0]
print("Weg: ", weg)

section = sections[1].split("\n")
netzwerk = {}
nw = {}

for s0 in section:
    s1 = s0.split(" = ")
    wegmarker = s1[0]
    s2 = s1[1].split(", ")
    sL = s2[0].replace("(", "")
    sR = s2[1].replace(")", "")
#    print("wegmarke:", wegmarker, " Links: ", sL, " Rechts: ", sR)
    nw = {"L": sL, "R": sR}
#    print(wegmarker)
    netzwerk[wegmarker] = nw
#    print(netzwerk[wegmarker])
#    print(netzwerk)
    
print("Das Gesamte Netzwerk sieht so aus: ", netzwerk)
#print(netzwerk["BBB"]["L"])


location_list = []
for key in netzwerk:
    if key[2] == "A":
        location_list.append(key)
print("Alle Startpunkte mit A am Ende", location_list)

a = 0
steps = 0
step_list = []

for location in location_list: 
    steps = 0
    while location[2] != "Z":   # hier nur letztes Zeichen auf Z prüfen
    #    print("Wegstrecke: ", weg[a])

        location = netzwerk[location][weg[a]]
    #    print(netzwerk[location][weg[a]])

    #    print("Nächster Punkt:", location)
    #    print("Abbiegen nach", weg[a])

        steps +=1
        #hochzählen und von vorn anfangen, wenn am Ende
        if a < len(weg)-1:
            a = a+1
        else:
            a = 0

#    print("----------")
#    print("Anzahl steps: ", steps)
    step_list.append(steps)

print(step_list)  # enthält die Liste der Anzahl Schritte, die die Geister jeweils benötigen
ergebnis = kgv_von_liste(step_list)  # ruft die kgv Funktion auf

print(f"Das kleinste gemeinsame Vielfache von {step_list} ist {ergebnis}")

