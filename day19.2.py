### Teil 1, Beispiel tut
### UNSUCCESSFUL
### Kudos an ChatGPT, für den Umbau meiner Dictionaries in Tuple. Lösung weiterhin falsch :-( 


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

    string = string[1: len(string)-1]
    string_liste = string.split(",")
    for eintrag in string_liste:
        key, value = eintrag.split("=")
        dic[key] = int(value)
        
    return dic


def workflow_dic_aus_liste(data):
    """
    Erstellt ein Dictionary aus einer Liste mit den gegebenen Workflows.
    Jeder Workflow wird als Liste von Tuples gespeichert.
    Durch ChatGPT umgebaut
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
    Liest einen Workflow ein und gibt eine Liste von Tuples zurück.
    Jedes Tuple repräsentiert eine Bedingung und den zugehörigen nächsten Workflow.
    Durch ChatGPT umgebaut
    """
    tuples_list = []
    for bed in wf:
        zeichen = ""
        if ":" in bed:
            key = bed[0]
            cond, nwf = bed.split(":")
            zeichen = cond[1]
            cond = int(cond[2:])
        else:
            key = "xxxx"
            cond = ""
            nwf = bed
        tuples_list.append((key, zeichen, cond, nwf))
    return tuples_list


def material_in_wf(workflow, materialtyp, matval):
    """
    Ermittelt den nächsten Workflow aus einem Workflow, dem Material und dem Materialwert.
    Berücksichtigt alle Bedingungen für einen Materialtyp, bevor zu einem anderen übergegangen wird.
    Durch ChatGPT umgebaut
    """
    enthalten = False
    newf = ""

    # Durchsuche alle Bedingungen für den gegebenen Materialtyp
    for tuple in workflow:
        if tuple[0] == materialtyp:
            if tuple[1] == "<" and matval < tuple[2]:
                newf = tuple[3]
                enthalten = True
                break
            elif tuple[1] == ">" and matval > tuple[2]:
                newf = tuple[3]
                enthalten = True
                break

    # Wenn keine Bedingung für den gegebenen Materialtyp erfüllt ist, verwende den Standardworkflow
    if not enthalten:
        for tuple in workflow:
            if tuple[0] == "xxxx":
                newf = tuple[3]
                break

    return newf, enthalten





file = "AOC_day19_input.txt"
workflows_inp, materials_inp = einlesen(file)
workflow_dic = workflow_dic_aus_liste(workflows_inp)
materials = []
for line in materials_inp:
    materials.append(part_read(line))
workflows = workflow_dic

#print("workflows", workflows)
#print(" ")
#print("materials", materials)
#print(" ")

t_val = 0

for line in materials:

    wf_no = "in"
    
    while True:
        key = ""
        print("material", line)
        print("workflow", wf_no, workflows[wf_no])

        for key in line:
            enth = False
            nwf_no, enth = material_in_wf(workflows[wf_no], key, line[key])
            if enth == True:
                break        
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

#    print(key, line[key], nwf_no, enth)
    print(" ")

# wf_no = neue WF no wenn enthalten = true
print("total value", t_val)

print("workflows:", len(workflows_inp), " wf_dic:", len(workflow_dic), " wf_dic2:", len(workflows), " materials:", len(materials_inp))



