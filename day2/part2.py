
import functools

f = open('data.txt', 'r')


def parse_input(line):
    game_index = int(line.split(':')[0].split(' ')[1].strip())
    games = line.split(':')[1].strip().split(';')
    games = [game.strip().split(',') for game in games]
    games = [[draw.strip().split(' ') for draw in game] for game in games]
    games = [functools.reduce(
        lambda acc, y: {**acc, y[1]: int(y[0])}, game, {}) for game in games]
    return game_index, games


def min_pow_game(game):
    mr = 0
    mg = 0
    mb = 0
    for draw in game:
        if draw.get("red", 0) > mr:
            mr = draw.get("red", 0)
        if draw.get("green", 0) > mg:
            mg = draw.get("green", 0)
        if draw.get("blue", 0) > mb:
            mb = draw.get("blue", 0)
    return mr * mg * mb


result = 0
for line in f:
    gid, games = parse_input(line)
    game_pow = min_pow_game(games)
    result += game_pow
    print(f"{gid}: {game_pow}")

print(f"Result: {result}")
