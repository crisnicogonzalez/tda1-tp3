def determinate_the_higher_flow_edges(graph):
    residual_graph = graph[:][:]
    while there_is_residual_flow(residual_graph):
        current_node = get_root(residual_graph)
        path = []
        while current_node_is_not_t(current_node):
            adyacents = get_adyacent_from(current_node)
            sorted_adyacents = sort_by_resisual_flow(adyacents)
            path.append(sorted_adyacents[0])

        minimun_flow_residual = minimun_flow_residual_from_path(path)
        update_flow_residual_in_residual_graph(residual_graph, minimun_flow_residual)
    sorted_residual_flows = get_sorted_residual_flow_by_desc(residual_graph)
    return sorted_residual_flows[:2]
