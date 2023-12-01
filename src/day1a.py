file = open("input/day1", "r")

calibration_values: list[int] = []

for line in file:
    numbers: list[int] = []
    for char in line:
        if not char.isnumeric():
            continue
        numbers.append(int(char))
    
    calibration_values.append(numbers[0] * 10 + numbers[-1])

print(sum(calibration_values))


