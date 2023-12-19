### und nochmal Teil 1, jetzt mit eval Funktion
### leider immer noch UNERFOLGREICH
### Beispiel tut, Puzzel nicht

def einlesen(filename):
    """
    liest alle Zeilen eines Textfiles ein und speichert jede einzelne Zeile in einer Liste
    """
    i = 0
    document = []
    document2 = []
    
    with open(filename, "r") as file:
        # read file line by line and output the lines
        for line in file:
            line = line.strip()
            if line == "":
                i = 1
            if i == 0:
                document.append(line)
            else:
                document2.append(line)
    document2.pop(0)
    
    return document, document2

def part_read(string):

    string_liste = []
    dic = {}

#    string = string[1: len(string)-1]
    string = string.strip("{")
    string = string.strip("}")
    string_liste = string.split(",")
    for eintrag in string_liste:
        key, value = eintrag.split("=")
        dic[key] = int(value)
        
    return dic

def workflow_dic_aus_liste(data):
    """
    erstellt ein Dictionary aus einer Liste mit den gegebenen Workflows
    """
    dic = {}
    for eintrag in data:
        key, values = eintrag.split("{")
        values = values.strip("}")
        vals = values.split(",")
        dic[key] = workflow_einlesen(vals)
        
    return dic

def workflow_einlesen(wf):
    """
    liest einen einzelnen flow aus einem Workflow ein und gibt eine Liste zurück
    """
    liste = []
    for bed in wf:
        zeichen = ""
        iliste = []
        if ":" in bed:
            cond, nwf = bed.split(":")
            iliste.append(cond)
            iliste.append(nwf)
            liste.append(iliste)
        else:
            liste.append(bed)

    return liste

def next_wf(workflow, material):
    """
    ermittelt den nächsten WF aus der Materialliste und dem Workflow
    """

    for key in material:
    #    print(key, material[key])

        for bed in workflow[0:len(workflow)-1]:
            x = m = a = s = 0
            nwfl = workflow[-1]

            if key in bed[0]:
                if key == "x":
                    x = material[key]
                elif key == "m":
                    m = material[key]
                elif key == "a":
                    a = material[key]
                elif key == "s":
                    s = material[key]

                if eval(bed[0]) == True:
                    nwfl = bed[1]
                    break

        if nwfl != workflow[-1]:
            break 

    return nwfl

###

file = "AOC_day19_input_bsp.txt"
workflows_inp, materials_inp = einlesen(file)
workflow_dic = workflow_dic_aus_liste(workflows_inp)
materials = []

for line in materials_inp:
    materials.append(part_read(line))
workflows = workflow_dic


#print("MAT: ", materials)  #dictionary mit materials fertig
#print("WF: ", workflows)   #workflows jetzt auch fertig


t_val = 0

for line in materials:

    wf_no = "in"
    
    while True:
        key = ""
        print("material", line)
        print("workflow", wf_no, workflows[wf_no])

        for key in line:
            enth = False
            nwf_no = next_wf(workflows[wf_no], line)     
        wf_no = nwf_no
        
        if nwf_no == "A":
            l_val = 0
            for key in line:
                l_val += line[key]
            t_val = t_val + l_val
            print("ACCEPTED", l_val, "für", line)
            print(" ")
            break
            
        elif nwf_no == "R":
            print("REJECTED")
            print(" ")
            break
            
        print("nächster Workflow", wf_no)
        print(" ")

    print(" ")

print("total value", t_val)
