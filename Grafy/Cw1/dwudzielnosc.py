from queue import Queue

def bfs(graph, root):
    n = len(graph)
    q = Queue()
    colors = [-1 for _ in range(n)]
    q.put(root)
    colors[root]=1
    
    for i in range(n):
        counter = 1
        prev = 1
        while not q.empty():
            counter+=1
            current = 0
            for i in range(prev):
                u = q.get()
                for v in graph[u]:
                    if colors[v]==-1:
                        colors[v]=counter%2
                        q.put(v)
                        current+=1
                    elif colors[v]!=counter%2:
                        return False
            prev = current

        if colors[i]==-1:
            q.put(i)
            colors[i]=1

    return True

#graph = [[1,3],[0,4,3],[3,5],[0,2,1],[1],[2]]
#graph = [[1,3],[0,4],[3,5],[0,2],[1],[2],[]]
graph = [[],[2,3],[1],[1]]
print(bfs(graph, 0))
