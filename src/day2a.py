file = open("input/day2", "r")

red: int = 12
green: int = 13
blue: int = 14

possible_games: list[int] = []

for line in file:
    # get game id
    game_id: int = int(line.split(':')[0].split(' ')[1])
    game_possible: bool = True

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

        # verify if combo is possible
        if (rgb.get('r', 0) > red or rgb.get('g', 0) > green or rgb.get('b', 0) > blue):
            game_possible = False
            break

    if (game_possible):
        possible_games.append(game_id)

print(sum(possible_games))
