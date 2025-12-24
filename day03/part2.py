import os

FILE_NAME = os.path.join(os.getcwd(), "day03", "data.txt")

file = open(FILE_NAME, "r")


def find_first_max_val(line: str, start_idx: int, stop_idx: int) -> (int, int):
    max_val, max_val_idx = 0, 0
    for i in range(start_idx, stop_idx + 1):
        v = int(line[i])
        if v > max_val:
            max_val = v
            max_val_idx = i

    return max_val, max_val_idx


joltages = []
for line in file:
    line = line.strip()
    current_joltage = ""
    last_idx = -1

    for i in range(12, 0, -1):
        max_val, max_val_idx = find_first_max_val(line, last_idx + 1, len(line) - i)
        current_joltage += str(max_val)
        last_idx = max_val_idx

    joltages.append(int(current_joltage))

print(sum(joltages))
