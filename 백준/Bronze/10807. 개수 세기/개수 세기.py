n = int(input())
arr = list(map(int, input().split()))
x = int(input())

cnt = 0

for i in range(n):
    if arr[i] == x:
        cnt += 1

print(cnt)