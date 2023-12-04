with open('./day02/day02.txt', 'r') as file:
    lines = file.readlines()

games = [line.strip() for line in lines]

test_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

class Game:
    def __init__(self, game):
        self.raw_game = game
        self.number = self.parse_game_number()
        self.rounds = self.parse_game_rounds()
    
    def parse_game_number(self):
        game_slice = self.raw_game.split(":")[0]
        number = ''
        for char in game_slice:
            if char.isdigit():
                number += str(char)
        return number

    def parse_game_rounds(self):
        game_slice = self.raw_game.split(": ")[1]
        rounds = game_slice.split("; ")
        parsed_rounds = []
        for round in rounds:
            cubes = round.split(", ")
            parsed_cubes = {}
            for cube in cubes:
                count = cube.split(" ")[0]
                color = cube.split(" ")[1]
                parsed_cubes[color] = count
            parsed_rounds.append(parsed_cubes)
        return parsed_rounds

#[{'green': '1', 'blue': '2'}, {'blue': '15', 'red': '12', 'green': '2'}, {'red': '4', 'blue': '6'}, {'blue': '10', 'red': '8'}, {'red': '3', 'blue': '12'}, {'green': '1', 'red': '12', 'blue': '8'}]
def test_games():
    count = 0
    for game in games:
        parsed_game = Game(game)
        is_exceeding = False
        for round in parsed_game.rounds:
            if is_exceeding:
                break
            is_exceeding = False
            for key, value in round.items():
                if int(value) > test_cubes[key]:
                    is_exceeding = True
                    break
        if not is_exceeding:
            count += int(parsed_game.number)
    print(count)

#test_games()

def find_highest_counts(rounds):
    highest_green = highest_red = highest_blue = 0

    for entry in rounds:
        if 'green' in entry:
            highest_green = max(highest_green, int(entry['green']))
        if 'red' in entry:
            highest_red = max(highest_red, int(entry['red']))
        if 'blue' in entry:
            highest_blue = max(highest_blue, int(entry['blue']))

    return [highest_green, highest_red, highest_blue]


def calculate_powers():
    total = 0
    for game in games:
        parsed_game = Game(game)
        highest_counts = find_highest_counts(parsed_game.rounds)
        result = highest_counts[0] * highest_counts[1] * highest_counts[2]
        total += result
    print(total)

calculate_powers()