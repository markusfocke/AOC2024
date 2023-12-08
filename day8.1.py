# Teil 1, successful

filename = "AOC_day8_input_bsp2.txt"

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
    print("wegmarke:", wegmarker, " Links: ", sL, " Rechts: ", sR)
    nw = {"L": sL, "R": sR}
    print(wegmarker)
    netzwerk[wegmarker] = nw
#    print(netzwerk[wegmarker])
#    print(netzwerk)
    
#print("Das Gesamte Netzwerk sieht so aus: ", netzwerk)
#print(netzwerk["BBB"]["L"])


# und hier laufen wir den Weg ab

location = "AAA"
a = 0
steps = 0


while location != "ZZZ":
    print("Wegstrecke: ", weg[a])
    
    location = netzwerk[location][weg[a]]
    print(netzwerk[location][weg[a]])
    
    print("Nächster Punkt:", location)
    print("Abbiegen nach", weg[a])

    steps +=1
    #hochzählen und von vorn anfangen, wenn am Ende
    if a < len(weg)-1:
        a = a+1
    else:
        a = 0

print("----------")
print("Anzahl steps: ", steps) 
