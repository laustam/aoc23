from functools import reduce

file = open("input/day6", "r")

times: list[int] = [int(num) for num in file.readline().split(':')[1].split(" ") if num.strip()]
distances: list[int] = [int(num) for num in file.readline().split(':')[1].split(" ") if num.strip()]
winning_count: list[int] = [0] * len(times)

for i in range(len(times)):
    time_limit: int = times[i]
    top_dist: int = distances[i]

    for button_press in range(time_limit):
        if (button_press * (time_limit - button_press) > top_dist):
            winning_count[i] += 1

print(reduce(lambda x,y: x*y, winning_count))