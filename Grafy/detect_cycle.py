def dfs(graph, root, visited, parent):
    visited[root]=True
    for v in graph[root]:
        if not visited[v]:
            parent[v]=root
            return dfs(graph, v, visited, parent)
        elif visited[v] and parent[root] != v:
            return True
    return False

def detect_cycle(graph, root):
    visited = [False]*len(graph)
    parent = [None]*len(graph)
    return dfs(graph, root, visited, parent)


graph1 = [[1, 2, 3], [0, 7], [0, 5], [0, 5], [0, 6, 7], [2, 3, 6], [4, 5], [1, 4]]
print(detect_cycle(graph1, 0))

# graph doesn't have a cycle
graph2 = [[1, 2, 5], [0, 3], [0, 4, 7, 8], [1], [2, 6], [0], [4], [2], [2]]
print(detect_cycle(graph2, 0))