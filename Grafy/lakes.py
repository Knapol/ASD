from queue import Queue

def dfs(T, visited, row, col, size):
    n = len(T)
    if row < 0 or row >= n or col < 0 or col >= n or T[row][col]=="L" or visited[row][col]:
        return size
    else:
        size+=1
        visited[row][col]=True
    
    actual_size = size
    actual_size = dfs(T, visited, row+1,col, actual_size)
    actual_size = dfs(T, visited, row-1,col, actual_size)
    actual_size = dfs(T, visited, row,col-1, actual_size)
    actual_size = dfs(T, visited, row,col+1, actual_size)

    return actual_size

def lakes(T):
    n=len(T)
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    biggest_lake = 0
    counter = 0

    for i in range(n):
        for j in range(n):
            if T[i][j]=="W" and not visited[i][j]:
                counter+=1
                biggest_lake = max(dfs(T, visited, i, j, 0), biggest_lake)
    return counter, biggest_lake

def bfs(T, row, col):
    n = len(T)
    prev_lands = 1

    q = Queue()
    visited = [[False for _ in range(n)] for _ in range(n)]

    q.put((row, col))
    visited[row][col] = True

    directions = [(0,1), (0,-1), (1,0),(-1,0)]
    counter = 2
    
    while not q.empty():
        lands = 0
        for i in range(prev_lands):
            u = q.get()
            for v in directions:
                row, col = u[0]+v[0], u[1]+v[1]

                if row == n-1 and col == n-1:
                    return True, counter
                
                if row >= 0 and row < n and col >=0 and col < n and T[row][col]=="L" and not visited[row][col]:
                    visited[row][col]=True
                    q.put((row, col))
                    lands+=1

        counter += 1
        prev_lands = lands

T = [["L", "W", "L", "L", "L", "L", "L", "L"],
     ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"],
     ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"],
     ["L", "W", "L", "L", "L", "L", "W", "W"],
     ["W", "W", "L", "W", "W", "L", "W", "L"],
     ["L", "L", "L", "W", "L", "L", "L", "L"]]

print(lakes(T))
print(bfs(T, 0, 0))