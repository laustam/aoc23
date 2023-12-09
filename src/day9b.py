file = open("input/day9", "r")

def get_prediction(history: list[int]) -> int:
    differences: list[int] = history
    prediction: int = differences[0]
    minus: bool = True # variate between adding and subtracting values
    while not all(diff == 0 for diff in differences):
        new_differences: list[int] = []
        i: int = 1 
        while i < len(differences):
            new_differences.append(differences[i] - differences[i-1])
            i+=1
        differences = new_differences
        prediction += -differences[0] if minus else differences[0]
        minus = not minus
    return prediction

sum_predictions: int = 0

for line in file:
    history: list[int] = [int(num) for num in line.split(" ")]
    sum_predictions += get_prediction(history=history)
print(sum_predictions)