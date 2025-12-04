import os

FILE_NAME = os.path.join(os.getcwd(), "day04", "data.txt")


def prepare_grid():
    first_line = file.readline().strip()
    grid = [list('.' * (len(first_line) + 2)), list('.' + first_line + '.')]

    for line in file:
        grid.append(list('.' + line.strip() + '.'))

    grid.append(list('.' * (len(first_line) + 2)))

    return grid


def number_of_adjacent_paper_rolls(grid, i ,j):
    count = 0
    for k in range(i-1, i+2):
        for n in range(j-1, j+2):
            if grid[k][n] == '@' and not (k == i and n == j):
                count += 1

    return count


file = open(FILE_NAME, 'r')

grid = prepare_grid()

accessible_paper_rolls_count = 0;
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if grid[i][j] == '@' and number_of_adjacent_paper_rolls(grid, i, j) < 4:
            accessible_paper_rolls_count += 1

for row in grid:
    print(row)

print('\n', accessible_paper_rolls_count)