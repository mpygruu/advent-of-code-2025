import os

import numpy as np

FILE_NAME = os.path.join(os.getcwd(), "day06", "data.txt")

file = open(FILE_NAME, "r")

worksheet = []
for line in file:
    worksheet.append(list(line[::-1]))


numbers = np.array(worksheet[:-1]).T
numbers = np.delete(numbers, 0, axis=0)
operations = worksheet[-1]

total_sum = 0
current_numbers = []
for line in zip(numbers, operations):
    number_str = "".join(line[0]).strip()
    if number_str == "":
        continue

    number = int(number_str)
    op = line[1]

    current_numbers.append(number)

    if op in {"*", "+"}:
        total_sum += np.prod(current_numbers) if op == "*" else np.sum(current_numbers)
        current_numbers = []

print(total_sum)
