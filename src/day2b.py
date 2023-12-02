file = open("input/day2", "r")

powers: list[int] = []

for line in file:
    min_rgb: dict = dict()

    # store colors and counts
    for turn in line.split(':')[1].split(';'):
        rgb: dict = dict()
        for combo in turn.split(','):
            count, color = combo.strip().split(' ')
            count = int(count)

            match color:
                case "red":
                    rgb['r'] = rgb.get('r', 0) + count

                case "green":
                    rgb['g'] = rgb.get('g', 0) + count

                case "blue":
                    rgb['b'] = rgb.get('b', 0) + count

        # update min rgbs
        min_rgb['r'] = max(rgb.get('r', 0), min_rgb.get('r', 0))
        min_rgb['g'] = max(rgb.get('g', 0), min_rgb.get('g', 0))
        min_rgb['b'] = max(rgb.get('b', 0), min_rgb.get('b', 0))

    powers.append(min_rgb.get('r', 1) * min_rgb.get('g', 1) * min_rgb.get('b', 1))

print(sum(powers))
