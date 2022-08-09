import sys

n = int(input())
arr = [sys.stdin.readline().strip() for _ in range(n)]

result = list(arr[0])

for i in range(n-1):
    for j in range(len(arr[0])):
        if arr[i][j] != arr[i+1][j]:
            result[j] = '?'

print(''.join(result))