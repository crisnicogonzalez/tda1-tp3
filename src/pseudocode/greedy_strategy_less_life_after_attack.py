def select(ships, damage_table, board):
    file_after_attack_by_ship = {}
    for ship in ships:
        damage_from_ship = damage_table.get_damage_from_pos(ship.get_pos_x(), ship.get_pos_y()+1)
        file_after_attack_by_ship[ship] = ship.get_life_points() - damage_from_ship
    lower_life_ship = get_lower_file(file_after_attack_by_ship)
    board.attack_to_position(lower_life_ship.get_pos_x(), lower_life_ship.get_pos_y()+1)
