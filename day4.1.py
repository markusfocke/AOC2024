file = "AOC_day4_input_bsp.txt"
document1 = []
document2 = []
total_worth = 0


def einlesen(filename):
    """
    liest alle Zeilen eines Textfiles ein und speichert jede einzelne Zeile in einer Liste
    """
    with open(filename, "r") as file:
        # read file line by line and output the lines
        numbers = []
        
        for line in file:
            line = line.strip()
            line = line.replace("  ", " ")
            line = line.split(": ")
            numbers = line[1].split(" | ")
            numbers[0] = numbers[0].split(" ")
            numbers[1] = numbers[1].split(" ")
            document1.append(numbers[0])
            document2.append(numbers[1])
    return document1, document2
                          
def listenvergleich(liste1, liste2):

    line_worth = 0
    w = 0
    a = 0 
    for element in liste1:
        if element in liste2:
            w = w + 1
        a = a + 1
    if w > 0:
        line_worth = 2**(w-1) 

    return line_worth 


einlesen(file)

for i in range(len(document1)):
    print(document1[i])
    print(document2[i])
    print("line worth: ", listenvergleich(document1[i], document2[i]))
    total_worth = total_worth + listenvergleich(document1[i], document2[i])

print("Total Worth of all Cards: ", total_worth)
