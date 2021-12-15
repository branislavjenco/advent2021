import copy

from utils import file_into_string

data = file_into_string("day6/input.txt")
data = [int(x) for x in data.split(",")]

period = 256
ages = [0 for _ in range(9)]

for fish in data:
    ages[fish] += 1

def tick(ages):
    tmp = copy.copy(ages)
    new_offspring_count = tmp[0]
    for i in range(1, len(tmp)):
        j = i - 1
        ages[j] = tmp[i]
    ages[8] = new_offspring_count
    ages[6] += new_offspring_count
    return ages

print("initial", ages)
for day in range(period):
    tick(ages)
    print(f"After {day + 1}: ", ages)
print(sum(ages))
