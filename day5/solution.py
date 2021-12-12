from utils import file_into_list
import pprint


data = file_into_list("day5/input.txt")


def parse_line(line):
    return [[int(x)for x in part.strip().split(",")] for part in line.split("->")]


def is_non_diagonal(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


data = [parse_line(line) for line in data]

filtered_data = [line for line in data if is_non_diagonal(line)]


def find_max_coord(data):
    total_max_x = 0
    total_max_y = 0
    for line in data:
        max_x = max(line[0][0], line[1][0])
        if max_x > total_max_x:
            total_max_x = max_x
        max_y = max(line[0][1], line[1][1])
        if max_y > total_max_y:
            total_max_y = max_y
    return total_max_x, total_max_y


def get_line_coverage(line):
    start, end = sorted(line)
    is_i_descending = start[0] > end[0]
    is_j_descending = start[1] > end[1]

    if is_i_descending:
        i_s = list(range(start[0], end[0] - 1, -1))
    else:
        i_s = list(range(start[0], end[0] + 1))

    if is_j_descending:
        j_s = list(range(start[1], end[1] - 1, -1))
    else:
        j_s = list(range(start[1], end[1] + 1))

    if len(i_s) == 1:
        i_s = [i_s[0] for _ in j_s]
    if len(j_s) == 1:
        j_s = [j_s[0] for _ in i_s]
    coverage = list(zip(i_s, j_s))
    return coverage


def mark_vent(line, diagram):
    coverage = get_line_coverage(line)
    for (i, j) in coverage:
        diagram[i][j] += 1


def count_dangerous_areas(diagram):
    count = 0
    for i in range(len(diagram)):
        for j in range(len(diagram[0])):
            if diagram[i][j] > 1:
                count += 1
    return count


def transpose(diagram):
    len_x = len(diagram)
    len_y = len(diagram[0])
    transposed = [[0 for j in range(len_y)] for i in range(len_x)]
    for i in range(len(diagram)):
        for j in range(len(diagram[0])):
            transposed[j][i] = diagram[i][j]
    return transposed



def print_diagram(diagram):
    for line in transpose(diagram):
        print("".join([str(x) if x != 0  else "." for x in line]))

def part_1(data):
    max_x, max_y = find_max_coord(data)
    diagram = [[0 for j in range(max_y + 1)] for i in range(max_x + 1)]
    for line in data:
        print(line)
        mark_vent(line, diagram)
    return count_dangerous_areas(diagram)


print("Part 1: ", part_1(filtered_data))
print("Part 2: ", part_1(data))




