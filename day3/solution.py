from utils import file_into_list


test = file_into_list("day3/test.txt")
report = file_into_list("day3/input.txt")

data = report

gamma_rate = []
epsilon_rate = []

for i in range(len(data[0])):
    zeros = 0
    ones = 0
    for entry in data:
        if entry[i] == "0":
            zeros += 1
        if entry[i] == "1":
            ones += 1
    if zeros > ones:
        gamma_rate.append("0")
        epsilon_rate.append("1")
    else:
        gamma_rate.append("1")
        epsilon_rate.append("0")
gamma_rate = int("".join(gamma_rate), 2)
epsilon_rate = int("".join(epsilon_rate), 2)

print("Part 1 ",gamma_rate * epsilon_rate)




i = 0
while len(data) > 1:
    new_data = []
    if i > (len(data[0]) - 1):
        break

    sum_ = 0
    for entry in data:
        sum_ += int(entry[i])

    most_common_value = "1" if sum_ >= len(data)/2 else "0"

    for entry in data:
        if entry[i] == most_common_value:
            new_data.append(entry)

    data = new_data
    i += 1

oxygen_generator_rating = int(data[0], 2)

data = report
i = 0
while len(data) > 1:
    new_data = []
    if i > (len(data[0]) - 1):
        break

    sum_ = 0
    for entry in data:
        sum_ += int(entry[i])

    least_common_value = "1" if sum_ < len(data)/2 else "0"

    for entry in data:
        if entry[i] == least_common_value:
            new_data.append(entry)

    data = new_data
    i += 1

co2_scrubber_rating = int(data[0], 2)

print("Part 2: ", oxygen_generator_rating * co2_scrubber_rating)