file = open("input/day15", "r")

MULTIPLIER = 17
DIVIDER = 256

def HASH(label: str):
    res = 0
    for char in label:
        res = ((res + ord(char)) * MULTIPLIER) % DIVIDER
    return res

boxes: dict = {}

# fill boxes
for lens in file.readline().strip().split(','):
    label = lens.split('=')[0].split('-')[0]
    box_nr = HASH(label)

    if '=' in lens:
        focal_len = lens.split('=')[1]

        change_lens = False
        for i, box in enumerate(boxes.get(box_nr,[])):
            if label in box:
                boxes[box_nr][i] = [label, focal_len]
                change_lens = True
                break

        if not change_lens: # add new lens
            boxes[box_nr] = boxes.get(box_nr,[]) + [[label,focal_len]]

    elif '-' in lens:
        boxes[box_nr] = [elem for elem in boxes.get(box_nr,[]) if elem[0] != label]

# compute focusing power
total_foc_pow = 0
for box_nr, box in boxes.items():
    for slot, lense in enumerate(box):
        total_foc_pow += (box_nr+1) * (slot+1) * int(lense[1])

print(total_foc_pow)