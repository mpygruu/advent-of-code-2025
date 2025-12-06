import numpy as np
import os


FILE_NAME=os.path.join(os.getcwd(), "day06", "data.txt")

file = open(FILE_NAME, 'r')

worksheet = []
for line in file:
    worksheet.append(list(line.strip().split()))

numbers = np.array(worksheet[:-1], dtype=int).T
operations = worksheet[-1]

total_sum = 0
for i in range(len(numbers)):
    total_sum += np.prod(numbers[i]) if operations[i] == '*' else np.sum(numbers[i])

print(total_sum)