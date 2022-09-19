import sys

input = sys.stdin.readline
n, m = map(int, input().split())
rect = []

for _ in range(n):
    rect.append(input())

result = 0
flag = False
for size in range(min(n ,m)-1, -1, -1):
    for r in range(n):
        for c in range(m):
            if (r + size < n) and (c + size < m) and (rect[r][c] == rect[r][c+size] == rect[r+size][c] == rect[r+size][c+size]):
                result = (size+1)**2
                flag = True
    if flag:
        break
print(result)