### zwischenstand wegen Jupyiterproblem


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
    liest einen Workflow ein und gibt ein dictionary zurück
    """
    dic = {}
    for bed in wf:
        zeichen = ""
        if ":" in bed:
            key = bed[0]
            cond, nwf = bed.split(":")
            zeichen = cond[1]
            cond = int(cond[2:len(cond)])
        else:
            key = "xxxx"
            cond = ""
            nwf = bed
        dic[key] = zeichen, cond, nwf

    return dic


def part_read(string):

    string_liste = []
    dic = {}

    string = string[1: len(string)-1]
    string_liste = string.split(",")
    for eintrag in string_liste:
        key, value = eintrag.split("=")
        dic[key] = int(value)
        
    return dic


def material_in_wf(workflow, materialtyp, matval):
    """
    ermittelt den nächsten workflow aus einem workflow, dem material und dem materialwert
    """
    enthalten = False
    newf = ""
    if materialtyp in workflow:
        if workflow[materialtyp][0] == "<":
            enthalten = True
            if matval < workflow[materialtyp][1]:
                newf = workflow[materialtyp][2]
            else:
                materialtyp = "xxxx"
                newf = workflow[materialtyp][2]
        elif workflow[materialtyp][0] == ">":
            enthalten = True
            if matval > workflow[materialtyp][1]:
                newf = workflow[materialtyp][2]
            else:
                materialtyp = "xxxx"
                newf = workflow[materialtyp][2]
        
    else:
        materialtyp = "xxxx"
        newf = workflow[materialtyp][2]

    return newf, enthalten



file = "AOC_day19_input_bsp.txt"
workflows_inp, materials_inp = einlesen(file)
workflow_dic = workflow_dic_aus_liste(workflows_inp)
materials = []
for line in materials_inp:
    materials.append(part_read(line))
workflows = workflow_dic

print("workflows", workflows)
print(" ")
print("materials", materials)
print(" ")


for line in materials:
    wf_no = "in"
    
    for key in line:
        nwf_no, enth = material_in_wf(workflows[wf_no], key, line[key])
        if enth == True:
            wf_no = nwf_no
        print(key, line[key], wf_no)

# wf_no = neue WF no wenn enthalten = true
