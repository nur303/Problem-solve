#(3)
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3],
    6: [4]
}
houses_with_missing = [2, 5]
def dfs(node, visited):
    visited[node] = True
    missing_houses = []
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if neighbor in houses_with_missing:
                missing_houses.append(neighbor)
            missing_houses.extend(dfs(neighbor, visited))
    return missing_houses

def find_houses_with_missing_info(start_node):
    visited = {node: False for node in graph}
    result = []
    if start_node in houses_with_missing:
        result.append(start_node)
    result.extend(dfs(start_node, visited))
    return result
start_house = 1
houses_with_missing = find_houses_with_missing_info(start_house)
print("Houses with missing information:", houses_with_missing)
