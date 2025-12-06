import os

FILE_NAME=os.path.join(os.getcwd(), "day05", "data.txt")

file = open(FILE_NAME, 'r')

ranges = []
ingredient_ids = []
for line in file:
    if '-' in line:
        left, right = line.strip().split('-')
        ranges.append((int(left), int(right)))

    elif line != '\n':
        ingredient_ids.append(int(line.strip()))

fresh_ingredients_count = 0
for idx in ingredient_ids:
    for rang in ranges:
        left, right = rang
        if left <= idx <= right:
            fresh_ingredients_count += 1
            break

print(fresh_ingredients_count)
