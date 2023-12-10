filename = "AOC_day2_input.txt"
document = []
summe_mgl_game_ids = 0
i = 1

def possible_or_not(line):
    """
    ermittelt, ob die Spielzeile möglich ist
    """
    
    game = []
    farbe = ["red", "blue", "green"]
    max_wuerfel = {
        "red": 12,
        "blue": 14,
        "green": 13
    }

    possible = 0
    line = line.split(": ")
    game = line[1]
    print(line[0],":", line[1])
    runde = game.split("; ")
    for element in runde:
        zug = element.split(", ")
        for element2 in zug:
            wuerfel = element2.split(" ")
            wuerfel[0] = int(wuerfel[0])
            if wuerfel[0] > max_wuerfel[wuerfel[1]]:
                possible = possible + 1
#            print(wuerfel[1], wuerfel[0], max_wuerfel[wuerfel[1]])

    if possible == 0:
        rueckmeldung = 1
        print("möglich")
    else:
        rueckmeldung = 0
        print("unmöglich")
        
    return rueckmeldung

with open(filename, "r") as file:
    # read file line by line and output the lines
    for line in file:
        line = line.strip()
#        print(possible_or_not(line))
        print(" ")
        summe_mgl_game_ids = summe_mgl_game_ids + i * possible_or_not(line)
        i = i + 1

print("---------")        
print("Die Summe der Game IDs: ", summe_mgl_game_ids)

