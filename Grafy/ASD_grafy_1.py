from queue import Queue

def BFS(s, G):
    visited = [-1]*len(G)
    q = Queue()
    q.put((s,0))
    #visited[s] = True
    while not q.empty():
        v, w = q.get()
        for u in G[v]: #G[v] sąsiedzi
            #if not visited[u]:
            if visited[u]==-1:
                q.put((u,w+1))
                visited[u] = w
    
    return visited

def BFS_2(graph, root):
    queue = Queue()
    visited = [False] * len(graph)
    result = []
    queue.put(root)
    visited[root] = True
    
    while not queue.empty():
        u = queue.get()
        result.append(u)
        for v in graph[u]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True
    return result

def DFS(root, graph):
    visited = [False]*len(graph)
    result[root]
    def dfs_visit(u, graph, visited, result):
        visited[u]=True
        for v in graph[u]:
            if not visited[v]:
                result.append(v)
                dfs_visit(v, graph, visited, result)
    
    dfs_visit(root, graph, visited, result)
    return result

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited

graph = [[1, 8], [0], [3, 4, 5, 8], [2], [2, 7], [2, 6], [5, 8], [4, 6], [0, 2, 6]]

result = BFS_2(graph, 1)
print(result)

print(BFS(1, graph))

result1 = DFS(1, graph)
print(result1)

result2 = dfs(graph, 1, [])
print(result2)