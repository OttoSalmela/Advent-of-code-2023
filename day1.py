file = open('day1.txt', 'r')
input = file.read()
input += "\n" # added so that for loop catches also the last line of the input

sum = 0
array = []
for char in input:
    if char == "\n":
        num1 = int(array[0])
        num2 = int(array[-1])
        num1 = num1 * 10
        num = num1 + num2
        sum += num
        array = []
    if char.isnumeric():
        array.append(char)
            
print(sum)
