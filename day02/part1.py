import os

FILE_NAME=os.path.join(os.getcwd(), "day02", "data.txt")

file = open(FILE_NAME, 'r')
line = file.readline().strip()

ranges_str = line.split(",")
invalid_ids_sum = 0
for range_str in ranges_str:
    range_min, range_max = range_str.split('-')

    for prod_id in range(int(range_min), int(range_max) + 1):
        prod_id_str = str(prod_id)
        left = prod_id_str[:len(prod_id_str) // 2]
        right = prod_id_str[len(prod_id_str) // 2:]
            
        if left == right:
            invalid_ids_sum += prod_id

print(invalid_ids_sum)
