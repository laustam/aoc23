file = open("input/day6", "r")

time: int = int("".join([num for num in file.readline().split(':')[1].split(" ") if num.strip()]))
distance: int = int("".join([num for num in file.readline().split(':')[1].split(" ") if num.strip()]))

# find minimum button press
min_press: int = 0
for button_press in range(time):
    if(button_press * (time - button_press) > distance):
        min_press = button_press
        break

# find maximum button press
max_press: int = 0
for button_press in range(time-1, min_press, -1):
    if(button_press * (time - button_press) > distance):
        max_press = button_press
        break

print(max_press - min_press + 1)