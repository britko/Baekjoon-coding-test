import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    x, y = min(x, y), max(x, y)
    parent[y] = x

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
for _ in range(m):
    op, a, b = map(int, input().split())
    
    if op == 0:
        union(a, b)
    elif op == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')