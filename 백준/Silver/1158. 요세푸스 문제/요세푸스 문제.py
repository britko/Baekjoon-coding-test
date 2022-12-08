from collections import deque

n, k = map(int, input().split())

arr = deque([x for x in range(1, n+1)])
result = list()

while len(arr) != 0:
    for _ in range(k-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())

print(str(result).replace('[', '<').replace(']', '>'))