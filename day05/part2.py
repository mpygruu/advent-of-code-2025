import os

FILE_NAME=os.path.join(os.getcwd(), "day05", "data.txt")

file = open(FILE_NAME, 'r')

ranges = []
for line in file:
    if '-' in line:
        left, right = line.strip().split('-')
        ranges.append((int(left), int(right)))

ranges.sort()

for i in range(len(ranges)-1, 0, -1):
    first_left, first_right = ranges[i-1]
    second_left, second_right = ranges[i]

    if second_left <= first_right <= second_right:
        ranges[i-1] = (first_left, second_right)
        ranges.remove(ranges[i])

    elif second_right <= first_right:
        ranges.remove(ranges[i])

fresh_ingredients_count = 0
for rang in ranges:
    left, right = rang
    fresh_ingredients_count += (right - left) + 1

print(fresh_ingredients_count)
