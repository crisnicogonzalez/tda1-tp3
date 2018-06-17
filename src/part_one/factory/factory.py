from src.part_one.game.ship import Ship


def create_board_configuration_from_file(file_name):
    file = open('src/part_one/config/'+file_name, 'r')
    configuration = []
    ships_live_points = []
    damage_board = []
    for line in file:
        splited_line = line.split(' ')
        maped_list = list(map(lambda item: int(item), splited_line))
        ships_live_points.append(maped_list[0])
        damage_board.append(maped_list[1:])
        configuration.append(list(map(lambda item: int(item), splited_line)))
    return ships_live_points, damage_board


def create_ships(life_points):
    return list(map(lambda life_point: Ship(life_point), life_points))

