file = open('day2.txt', 'r')
lines = file.readlines()


sum = 0
game_num = 0
for line in lines:
    game_num += 1
    is_possible = True

    if "red" in line:
        locations = [i for i in range(len(line)) if line.startswith("red", i)]
        for location in locations:
            value = int(line[location-3:location-1])
            if value > 12:
                is_possible = False

    if "green" in line:
        locations = [i for i in range(len(line)) if line.startswith("green", i)]
        for location in locations:
            value = int(line[location-3:location-1])
            if value > 13:
                is_possible = False

    if "blue" in line:
        locations = [i for i in range(len(line)) if line.startswith("blue", i)]
        for location in locations:
            value = int(line[location-3:location-1])
            if value > 14:
                is_possible = False

    if is_possible == True:
        sum += game_num


print(sum)