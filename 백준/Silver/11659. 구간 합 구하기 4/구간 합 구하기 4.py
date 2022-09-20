import sys

input = sys.stdin.readline
_, m = map(int, input().split())

a = list(map(int, input().split()))
sum = [0] * 100001

for i in range(1, len(a) + 1):
    sum[0] = 0
    sum[i] = a[i-1] + sum[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])