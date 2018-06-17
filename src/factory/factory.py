from src.game.ship import Ship


def create_board_configuration_from_file(file_name):
    file = open(file_name, 'r')
    configuration = []
    for line in file:
        splited_line = line.split(' ')
        configuration.append(map(lambda item: int(item), splited_line))
    return configuration


def create_ships(life_points):
    return map(lambda life_point: Ship(life_point), life_points)

