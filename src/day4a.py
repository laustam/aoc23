file = open("input/day4", "r")

total_points: int = 0

for line in file:
    winning_numbers: set[int] = set([int(num) for num in line.split(':')[1].split('|')[0].strip().split(" ") if num.isnumeric()])
    my_numbers: set[int] = set([int(num) for num in line.split('|')[1].strip().split(" ") if num.isnumeric()])
    overlapping: set[int] = winning_numbers.intersection(my_numbers)
    total_points += pow(2, len(overlapping)-1) if len(overlapping) > 0 else 0

print(total_points)
