# Erster Versuch, brute force führt auch nach 120 min auf MBP M1 nicht zu einer Lösung


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
    
# print(netzwerk)

location_list = []

for key in netzwerk:
    if key[2] == "A":
        location_list.append(key)

print("Alle Startpunkte mit A am Ende", location_list)


a = 0
steps = 0
end_items = 0
        

while end_items != len(location_list):    # so lange bis alle Items der Liste ein Z am Ende enthalten
    
#    print("Wegstrecke: ", weg[a])
    for item in location_list:
        location = item 
        pos = location_list.index(item)
        location_list.pop(pos)
        location_list.insert(pos, netzwerk[location][weg[a]])
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
    
    end_items = 0
    for eintrag in location_list:
        if eintrag[2] == "Z":
            end_items +=1

print("----------")
print("Anzahl steps: ", steps) 
print("Endpunkte: ", location_list)
