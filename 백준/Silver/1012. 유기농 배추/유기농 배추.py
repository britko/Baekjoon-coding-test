from collections import deque

# 방향 벡터(상하좌우)
dir_vec = [[0,1], [0,-1], [-1,0], [1,0]]

# DFS를 사용하면 Recursion Error때문에 BFS사용
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in dir_vec:
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

# t: 테스트 케이스 개수
t = int(input())
for _ in range(t):
    # m: 배추밭 가로길이, n: 배추밭 세로길이, k: 배추 개수
    m, n, k = map(int, input().split())

    graph = [[0 for j in range(n)] for i in range(m)]
    # 배추 좌표 입력
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)