sections = []
seeds = []
seed2soil = []
soil2fert = []
fert2water = []
water2light = []
light2temp = []
temp2hum = []
hum2loc = []
location_min = 100**1000

filename = "AOC_day5_input.txt"

with open(filename, "r") as file:
        data_text = file.read()

#print(data_text)

sections = data_text.split("\n\n")
#sections = data_text.strip().split("\n\n")  
#print(sections)

for section in sections:

    if "seeds:" in section:
        s0 = section.split("seeds: ")[1]
        f = [int(num) for num in s0.split(" ")]
        seeds.extend(f)
              
    if "seed-to" in section:
        s0 = section.split("map:\n")
        s1 = s0[1].split("\n")
        for e in s1:
            f = e.split(" ")
            f = [int(num) for num in f]
            seed2soil.append(f)
    if "soil-to-fertilizer" in section:
        s0 = section.split("map:\n")
        s1 = s0[1].split("\n")
        for e in s1:
            f = e.split(" ")
            f = [int(num) for num in f]
            soil2fert.append(f)
    if "fertilizer-to-water" in section:
        s0 = section.split("map:\n")
        s1 = s0[1].split("\n")
        for e in s1:
            f = e.split(" ")
            f = [int(num) for num in f]
            fert2water.append(f)
    if "water-to-light" in section:
        s0 = section.split("map:\n")
        s1 = s0[1].split("\n")
        for e in s1:
            f = e.split(" ")
            f = [int(num) for num in f]
            water2light.append(f)
    if "light-to-temperature" in section:
        s0 = section.split("map:\n")
        s1 = s0[1].split("\n")
        for e in s1:
            f = e.split(" ")
            f = [int(num) for num in f]
            light2temp.append(f)
    if "temperature-to-humidity" in section:
        s0 = section.split("map:\n")
        s1 = s0[1].split("\n")
        for e in s1:
            f = e.split(" ")
            f = [int(num) for num in f]
            temp2hum.append(f)
    if "humidity-to-location" in section:
        s0 = section.split("map:\n")
        s1 = s0[1].split("\n")
        for e in s1:
            f = e.split(" ")
            f = [int(num) for num in f if num.strip()]
            hum2loc.append(f)

print("Seeds", seeds)      
print("S2S", seed2soil)
print("S2F", soil2fert)
print("f2W", fert2water)
print("w2l", water2light)
print("l2t", light2temp)
print("t2h", temp2hum)
print("h2l", hum2loc)

seedid = 0

def wertinliste(seedid, such_liste):
    startwert = 0
    abstand = 0
    ausgabewert = 0
    abschnitt = 0
    rueckgabewert = seedid
 
    for zeile in such_liste:
        startwert = zeile[1]
        ausgabewert = zeile[0]
        abstand = zeile[2]
        abschnitt = range(startwert, startwert + abstand)
        
        if seedid in abschnitt:   
            rueckgabewert = ausgabewert + (seedid-startwert)       
                
    return rueckgabewert

for seed in seeds: 
    soil = wertinliste(seed, seed2soil)
    fertilizer = wertinliste(soil, soil2fert)
    water = wertinliste(fertilizer, fert2water)
    light = wertinliste(water, water2light)
    temperature = wertinliste(light, light2temp) 
    humidity = wertinliste(temperature, temp2hum)
    location = wertinliste(humidity, hum2loc)
    print("seed", seed, 
         "soil", soil, 
         "fertilizer", fertilizer,
         "water", water,
         "light", light,
         "temperature", temperature,
         "humidity", humidity,
         "location", location)
    if location < location_min:
        location_min = location
print("Lowest location: ", location_min)

