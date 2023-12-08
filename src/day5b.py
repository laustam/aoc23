file = open("input/day5", "r")

def left_overlap(start, end, test_min, test_max): return test_min <= start and test_max > start and test_max < end

def right_overlap(start, end, test_min, test_max): return test_min > start and test_min < end and test_max >= end

def full_partial_overlap(start, end, test_min, test_max): return test_min > start and test_max < end

def full_complete_overlap(start, end, test_min, test_max): return test_min <= start and test_max > start and test_max >= end

def update_ranges(file, values: list[int]):
    file.readline()
    new_values: list[int] = []
    while True:
        line: str = file.readline()

        if not line or line == "\n":
            break

        dest_val, source_val, range_len = [int(val) for val in line.strip().split(" ")]
        offset: int = dest_val - source_val

        i = 0
        while i < len(values):
            start, end = values[i]
            test_min = source_val
            test_max = source_val + range_len - 1

            # if overlap: (1) add shifted range to new_values then (2) update ranges in original values
            if (left_overlap(start, end, test_min, test_max)):
                new_values.append([start+offset, test_max+offset])
                values[i] = [test_max+1, end]

            elif (right_overlap(start, end, test_min, test_max)):
                new_values.append([test_min+offset, end+offset])
                values[i] = [start, test_min-1]

            elif (full_partial_overlap(start, end, test_min, test_max)):
                new_values.append([test_min+offset, test_max+offset])
                values[i] = [start, test_min-1]
                values.append([test_max+1, end])

            elif (full_complete_overlap(start, end, test_min, test_max)):
                new_values.append([start+offset, end+offset])
                values.remove(values[i])
                continue # removed item at i, so want to check same position i again

            i += 1

    return new_values + values

values: list[int] = []
initial_seeds: list[int] = [int(val) for val in file.readline().strip().split(" ")[1:]]

i = 0
while i < len(initial_seeds):
    new_seed, new_range = initial_seeds[i], initial_seeds[i+1]
    values.append([new_seed, new_seed+new_range-1])
    i += 2

file.readline()

for _ in range(7):
    values = update_ranges(file, values)

print(min([item for item, _ in values]))