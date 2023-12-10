time = 60947882
c_distance = 475213810151650

button_time = 0
speed = 0
travel_time = 0
distance = 0
winning_ways = 0

    
for button_time in range(time):
    speed = button_time
    travel_time = time - button_time
    distance = travel_time * speed
    if distance > c_distance:
        winning_ways += 1
    
print("anzahl ww: ", winning_ways)
