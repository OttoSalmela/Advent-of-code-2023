file = open('Day3/Day3.txt', 'r')
lines = file.readlines()

array = []
for line in lines:
    line_array = []
    for char in line:
        if char != "\n":
            line_array.append(char)
    array.append(line_array)

stars = []
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == '*':
            stars.append([i,j])

numbers = []
number = []
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j].isnumeric():
            number.append[array[i][j]]
