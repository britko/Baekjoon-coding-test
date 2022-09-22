n = int(input())
e = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
def dfs(node):
    visited[node] = 1

    for i in graph[node]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(sum(visited)-1)   # 1번 컴퓨터 제외