def create_board_configuration_from_file(file_name):
    file = open(file_name, 'r')
    configuration = []
    for line in file:
        splited_line = line.split(' ')
        configuration.append(map(lambda item: int(item), splited_line))
    return configuration

