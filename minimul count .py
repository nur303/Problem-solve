#(4)
import heapq
graph = {
    1: [(2, 10), (3, 20)],
    2: [(1, 10), (4, 15)],
    3: [(1, 20), (5, 25)],
    4: [(2, 15), (6, 30)],
    5: [(3, 25)],
    6: [(4, 30)]

}

def prim_mst(graph):
    mst = []
    visited = set()
    start_node = next(iter(graph))
    priority_queue = [(0, start_node)]

    while priority_queue:
        weight, node = heapq.heappop(priority_queue)
        if node not in visited:
            visited.add(node)
            if weight > 0:
                mst.append((weight, node))
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_weight, neighbor))
    return mst
minimal_edges = prim_mst(graph)
print("Minimal edges for connecting all houses:", minimal_edges)
