from utils import file_into_list


l = [int(x) for x in file_into_list("day1/input.txt")]
count = 0
for i in range(1, len(l)):
    prev = l[i-1]
    curr = l[i]
    if curr > prev:
        count += 1
print("Part 1 ", count)


count = 0
measurements = []
for i in range(0, len(l) -2 , 1):
    measurements.append(l[i] + l[i+1] + l[i+2])

for i in range(1,len(measurements)):
    if measurements[i] > measurements[i-1]:
        count += 1

print("Part 2 ", count)
