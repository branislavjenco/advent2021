from utils import file_into_list

mapping = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
lengths = [len(el) for el in mapping]
print(lengths)

lines = file_into_list("day8/test1.txt")
lines = [line.split("|") for line in lines]
lines = [[line[0].strip().split(" "), line[1].strip().split(" ")] for line in lines]

count = 0
for line in lines:
    patterns, outputs = line
    for output in outputs:
        if len(output) in [2, 4, 7, 3]:
            count += 1

print("Part 1: ", count)

for line in lines:
    patterns, outputs = line
    current_mapping = set()
    for pattern in patterns:
        print(current_mapping)
        if len(pattern) == 2:
            for i in range(2):
                current_mapping.add((mapping[1][i], pattern[i]))
        elif len(pattern) == 3:
            for i in range(3):
                current_mapping.add((mapping[7][i], pattern[i]))
        elif len(pattern) == 4:
            for i in range(4):
                current_mapping.add((mapping[4][i], pattern[i]))
        elif len(pattern) == 7:
            for i in range(7):
                current_mapping.add((mapping[8][i], pattern[i]))
    print(current_mapping)
    print(len(current_mapping))




print(lines)