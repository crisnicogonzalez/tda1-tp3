def determinate_the_higher_flow_edges(graph):
    max_flow = aplicate_ford_fulkerson(graph)
    return get_sorted_edges_asc(max_flow)