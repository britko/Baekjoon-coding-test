import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

cnt = 0

for i in coins[::-1]:
    if k == 0:
        break

    if k - i >= 0:
        cnt += k // i
        k = k - k // i * i

print(cnt)