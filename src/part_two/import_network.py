from src.part_two.ADTs.grafo import Grafo

def file_to_network_graph(filename):
    g = Grafo(True)
    with open(filename,'r') as f:
        line = f.readline()
        while line:
            info = line.split(' ')
            g.add_vertice(int(info[0]))
            g.add_vertice(int(info[1]))
            g.add_or_update_arista(int(info[0]), int(info[1]), int(info[2].replace("\n","")))
            line = f.readline()
    matrix = [[0 for x in range(g.cantidadVertices)] for y in range(g.cantidadVertices)]
    for i in range(0,g.cantidadVertices):
        for j in range(0,g.cantidadVertices):
            matrix[i][j] = g.get_peso_arista(i, j) if g.get_peso_arista(i, j) else 0
        
    return matrix
        