import numpy as np

def FordFulkerson(source, sink, rows, residual_graph):
    parent = [-1] * rows
    max_flow = 0

    while get_BFS(source, sink, parent,rows,residual_graph):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
    return max_flow,residual_graph


# En parent tengo el camino
# Y devuelvo si es que t es visitado, si es asi, el path que devuelvo es
#augmentating path porque filtro aquellos que tiene val > 0, osea valor residual
def get_BFS(s, t, parent, row, graph):
    visited = [False]*row
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return True if visited[t] else False


def get_max_flows(flow_graph):
    flat_list = [item for sublist in flow_graph for item in sublist]
    return sorted(flat_list)


def get_paths_to_protect(graph, source, sink):
    max_flow, residual_graph = FordFulkerson(source, sink, len(graph), np.array(graph))
    flow_graph = graph - residual_graph
    max_flow_sortered = get_max_flows(flow_graph)
    return max_flow_sortered[:2]
