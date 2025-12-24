import os

FILE_NAME = os.path.join(os.getcwd(), "day03", "data.txt")

file = open(FILE_NAME, "r")


def find_first_max_val(line: str) -> (int, int):
    max_val, max_val_idx = 0, 0
    for i, v in enumerate(line):
        v = int(v)
        if v > max_val:
            max_val = v
            max_val_idx = i

    return max_val, max_val_idx


joltages = []
for line in file:
    line = line.strip()

    max_val, max_val_idx = find_first_max_val(line)

    if max_val_idx == len(line) - 1:
        tens_digit = max(line[:-1])
        joltages.append(int(f"{tens_digit}{max_val}"))
    else:
        ones_digit = max(line[max_val_idx + 1 :])
        joltages.append(int(f"{max_val}{ones_digit}"))

    print(line, joltages[-1])

print(sum(joltages))
