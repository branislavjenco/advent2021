import numpy as np
import math
from utils import file_into_string

data = [int(x) for x in file_into_string("day7/input.txt").split(",")]
data = np.array(data)
avg = int(data.mean())
minimal = math.inf

for avg in range(0, max(data)):
    s = 0
    for crab in data:
        fuel = abs(crab - avg)
        fuel = sum(range(1, fuel + 1))
        s += fuel
    if s < minimal:
        minimal = s
print(minimal)


