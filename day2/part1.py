
import functools

f = open('data.txt', 'r')

num_red = 12
num_green = 13
num_blue = 14


def parse_input(line):
    game_index = int(line.split(':')[0].split(' ')[1].strip())
    games = line.split(':')[1].strip().split(';')
    games = [game.strip().split(',') for game in games]
    games = [[draw.strip().split(' ') for draw in game] for game in games]
    games = [functools.reduce(
        lambda acc, y: {**acc, y[1]: int(y[0])}, game, {}) for game in games]
    return game_index, games


def check_game(game):
    for draw in game:
        if draw.get("red", 0) > num_red:
            return False
        if draw.get("green", 0) > num_green:
            return False
        if draw.get("blue", 0) > num_blue:
            return False
    return True


result = 0
for line in f:
    gid, games = parse_input(line)
    game_possible = "Possible" if check_game(games) else "Impossible"
    result += int(gid) if game_possible == "Possible" else 0
    print(f"{gid}: {game_possible}")

print(f"Result: {result}")
