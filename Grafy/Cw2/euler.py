# Znaleźć cykl eulera i go zwrócić; rep macierzowa

def DFS_visit(v, g, path):
    n = len(g)
    for i in range(n):
        if g[v][i] == 1:
            g[v][i] = g[i][v] = 0
            DFS_visit(i, g, path)
    path.append(v)

def euler(g):
    n = len(g)
    total = 0
    for i in range(n):
        total+=sum(g[i])

        if total%2 == 1:
            return False
    
    path = []
    DFS_visit(0, g, path)
    if total//2+1 != len(path):
        return False
    
    return path

g = [
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0]
]

print(euler(g))