file = open("input/day1", "r")

def isNumber(input: str) -> int:
    if input[0].isnumeric():
        return int(input[0])
    elif input.startswith("one"):
        return 1
    elif input.startswith("two"):
        return 2
    elif input.startswith("three"):
        return 3
    elif input.startswith("four"):
        return 4
    elif input.startswith("five"):
        return 5
    elif input.startswith("six"):
        return 6
    elif input.startswith("seven"):
        return 7
    elif input.startswith("eight"):
        return 8
    elif input.startswith("nine"):
        return 9
    else:
        return -1

calibration_sum = 0

for line in file:
    for i in range(len(line)):                    
        maybe_num = isNumber(line[i:])
        if maybe_num != -1:
            first_digit = maybe_num
            break
    
    for j in range(len(line)-1,-1,-1):        
        maybe_num = isNumber(line[j:])
        if maybe_num != -1:
            last_digit = maybe_num
            break

    calibration_sum += first_digit * 10 + last_digit

print(calibration_sum)