file = open("input/day4", "r")

total_scratchcards: int = 0
cards_to_process: list[int] = []
matching_nums: dict[int] = {}

for line in file:
    card_number: int = int(line.split(':')[0].split(" ")[-1])
    winning_numbers: set[int] = set([int(num) for num in line.split(':')[1].split('|')[0].strip().split(" ") if num.isnumeric()])
    my_numbers: set[int] = set([int(num) for num in line.split('|')[1].strip().split(" ") if num.isnumeric()])
    overlapping: set[int] = winning_numbers.intersection(my_numbers)
    matching_nums[card_number] = len(overlapping)
    cards_to_process.extend(list(range(card_number + 1, card_number + len(overlapping)+1)))
    total_scratchcards += 1

while len(cards_to_process) > 0:
    card_num: int = cards_to_process.pop()
    total_scratchcards += 1
    matching: int = matching_nums.get(card_num)
    cards_to_process.extend(list(range(card_num + 1, card_num + matching+1)))

print(total_scratchcards)

# too low 1032