file = open("input/day15", "r")

MULTIPLIER = 17
DIVIDER = 256

curr_val = 0
res_sum = 0

for char in file.readline().strip():
    if char == ',':
        res_sum += curr_val
        curr_val = 0
        continue

    curr_val = ((curr_val + ord(char)) * MULTIPLIER) % DIVIDER

print(res_sum + curr_val)