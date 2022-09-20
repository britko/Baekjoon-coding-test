import sys

input = sys.stdin.readline
n, m = map(int, input().split())

a = list(map(int, input().split()))
sum = []
sum.append(0)

for i in range(1, n+1):
    sum.append(a[i-1] + sum[i-1])

for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])