import networkx as nx
import matplotlib.pyplot as plt

def johnson_algorithm(G):
    s = "#"
    G.add_node(s)
    for node in G.nodes():
        G.add_edge(s, node, weight=0)

    dist = nx.single_source_bellman_ford_path_length(G, s)

    for u, v, weight in G.edges(data=True):
        weight["weight"] = weight["weight"] + dist[u] - dist[v]

    shortest_paths = {}
    for node in G.nodes():
        shortest_paths[node] = nx.single_source_dijkstra_path_length(G, node, weight="weight")

    for node in G.nodes():
        if node != s:
            if s in shortest_paths:
                shortest_paths.pop(s)
            for node in G.nodes():
                if node != s:
                    if s in shortest_paths:
                        shortest_paths.pop(s)
                    for node in G.nodes():
                        if node != s and node in shortest_paths:
                            if s in shortest_paths:
                                shortest_paths.pop(s)
                            for node in shortest_paths:
                                if node != s:
                                    shortest_paths[node].pop(s, None)
                            G.remove_node(s)
                            return shortest_paths
                    G.remove_node(s)
                    return shortest_paths
            G.remove_node(s)
            return shortest_paths
    G.remove_node(s)
    return shortest_paths
    
    dist, _ = nx.single_source_bellman_ford(G, s)

    for u, v, weight in G.edges(data=True):
        weight["weight"] = weight["weight"] + dist[u] - dist[v]

    shortest_paths = {}
    for node in G.nodes():
        shortest_paths[node] = nx.single_source_dijkstra_path_length(G, node, weight="weight")

    for node in G.nodes():
        shortest_paths[node].pop(s)
    G.remove_node(s)
    return shortest_paths

G = nx.DiGraph()
G.add_edge(1, 2, weight=4)
G.add_edge(1, 3, weight=2)
G.add_edge(2, 3, weight=1)
G.add_edge(2, 4, weight=-3)
G.add_edge(3, 5, weight=1)
G.add_edge(4, 5, weight=2)
G.add_edge(5, 2, weight=1)

shortest_paths = johnson_algorithm(G)
print(shortest_paths)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos)
plt.show()




