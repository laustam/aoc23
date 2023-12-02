file = open("input/day1", "r")

def isNumber(input: str) -> int:

    if input.startswith("one"):
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

calibration_values: list[int] = []

for line in file:
    numbers: list[int] = []
    for i in range(len(line)):
        char: chr = line[i]
        if not char.isnumeric():
            maybe_num: int = isNumber(line[i:])
            if maybe_num != -1:
                numbers.append(maybe_num)
            continue
        numbers.append(int(char))
    calibration_values.append(numbers[0] * 10 + numbers[-1])

print(sum(calibration_values))


