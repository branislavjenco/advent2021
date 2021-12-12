from utils import file_into_list


instructions = [(a[0], int(a[1])) for a in [x.split(" ") for x in file_into_list("day2/input.txt")]]
test = [(a[0], int(a[1])) for a in [x.split(" ") for x in file_into_list("day2/test.txt")]]


pos = 0
depth = 0

for d, steps in instructions:
    if d == "forward":
        pos = pos + steps
    if d == "down":
        depth = depth + steps
    if d == "up":
        depth = depth - steps

print("Part 1 ", pos * depth)

pos = 0
depth = 0
aim = 0

for d, steps in instructions:
    if d == "forward":
        pos = pos + steps
        depth = depth + (aim * steps)
    if d == "down":
        aim = aim + steps
    if d == "up":
        up = aim = aim - steps

print("Part 2 ", pos * depth)





