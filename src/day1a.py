file = open("input/day1", "r")

calibration_sum = 0

for line in file:
    for char in line:
        if char.isnumeric():
            first_digit = int(char)
            break
    for char in line[::-1]:
        if char.isnumeric():
            last_digit = int(char)
            break
    
    calibration_sum += first_digit * 10 + last_digit

print(calibration_sum)