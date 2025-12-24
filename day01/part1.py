import os

FILE_NAME = os.path.join(os.getcwd(), "day01", "data.txt")

file = open(FILE_NAME, "r")

number_of_zeros = 0
current_rotation = 50
for line in file:
    direction, rotation = line[0], int(line[1:].strip())

    if direction == "R":
        current_rotation = (current_rotation + rotation) % 100
    else:
        current_rotation = (current_rotation - rotation) % 100

    if current_rotation == 0:
        number_of_zeros += 1

file.close()

print(number_of_zeros)
