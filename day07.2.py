# Teil 2
# Successful

file = "AOC_day7_input.txt"
document = []


def einlesen(filename):
    """
    liest alle Zeilen eines Textfiles ein und speichert jede einzelne Zeile in einer Liste
    """
    with open(filename, "r") as file:
        # read file line by line and output the lines
        items = []
        for line in file:
            line = line.strip()
            items = line.split(" ")
            items[1] = int(items[1])
            document.append(items)
    return document
                          
einlesen(file)
#print(document)

def handtyp_bestimmen(setofcards):   #changed
    
    buben_anzahl = setofcards.count("J")
    cardset = setofcards.replace("J", "")
    
    if cardset == "":
        cardset = "JJJJJ"
        buben_anzahl = 0
    
    anzahlen = buchstaben_haeufigkeit(cardset)
    most_letter = max(anzahlen, key=anzahlen.get)
    most_letter_value = anzahlen[most_letter] + buben_anzahl 
    
    if most_letter_value == 5:
        hand = "5"
    elif most_letter_value == 4:
        hand = "4"
    elif most_letter_value == 3 and len(anzahlen) == 2:
        hand = "fh"
    elif most_letter_value == 3:
        hand = "3"    
    elif most_letter_value == 2 and len(anzahlen) == 3:
        hand = "2p"
    elif most_letter_value == 2:
        hand = "1p"
    else:
        hand = "1"
        
    return hand

def buchstaben_haeufigkeit(text):
    haeufigkeit = {}
    for buchstabe in text:
        if buchstabe in haeufigkeit:
            haeufigkeit[buchstabe] += 1
        else:
            haeufigkeit[buchstabe] = 1
    return haeufigkeit

def card_dic_create():

    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]   #Reihenfolge anders in teil2
    dic = {}
    rank = 1
    for card in cards[::-1]:
        dic[card] = hex(rank)[2:]
        rank +=1
    return dic

def hex_umwandlung(string):
    """
    wandelt einen String von Karten in eine Hexadezimalzahl um, die den jeweiligen Kartenrang symbolisiert
    """
    new_string = "0x"
    for buchstabe in string:
            new_string += card_strength[buchstabe]
    
    return new_string

def multisort(document, column1, column2):
    """
    sortiert eine Liste aufsteigend nach 2 Spalten (spalten nummer angeben)
    https://www.geeksforgeeks.org/sort-a-list-of-objects-by-multiple-attributes-in-python/
    """
    import operator
    doc_sorted = sorted(document, key = operator.itemgetter(column1, column2))
    
    return doc_sorted


def ranking_best(hd):
    
    ranking = {'5': 7,
              '4': 6,
              '3': 4,
              'fh': 5,
              '2p': 3,
              '1p': 2,
              '1': 1}
    
    return ranking[hd]

def return_rank(liste):
    return liste[2]
    
document2 = document
card_strength = card_dic_create()



for ele in document2:
    hand = handtyp_bestimmen(ele[0])
    rang = ranking_best(hand)
    ele.append(rang) #fügt den Rang nach der jeweiligen Hand zur Liste hinzu
    cardsrank = hex_umwandlung(ele[0])
    ele.append(cardsrank) #bildet eine hexzahl aus jeder einzelnen Karte um den hand-internen Rang zu bestimmen


#print(document2)

#document2.sort(key=return_rank)

document3 = multisort(document2, 2, 3)

#print(document3)

i = 1
t_win = 0

for item in document3:
    bid = item[1]
    win = i * bid
    t_win += win
#    print(item[0], i, "*", bid, "=", win, t_win)
    i +=1
    
print("total winnings", t_win)




