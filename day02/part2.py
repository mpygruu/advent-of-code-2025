import os

FILE_NAME = os.path.join(os.getcwd(), "day02", "data.txt")

file = open(FILE_NAME, "r")
line = file.readline().strip()

ranges_str = line.split(",")
invalid_ids_sum = 0
for range_str in ranges_str:
    range_min, range_max = range_str.split("-")

    for prod_id in range(int(range_min), int(range_max) + 1):
        prod_id_str = str(prod_id)
        already_found = []

        length = 1
        while length <= len(prod_id_str) // 2:
            possible_sequences = [
                prod_id_str[i : i + length] for i in range(0, len(prod_id_str), length)
            ]

            if len(set(possible_sequences)) == 1 and prod_id not in already_found:
                invalid_ids_sum += prod_id
                already_found.append(prod_id)

            length += 1

print(invalid_ids_sum)
