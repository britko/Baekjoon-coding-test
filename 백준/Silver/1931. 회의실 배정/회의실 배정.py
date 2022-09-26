import sys

input = sys.stdin.readline
n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x : (x[1], x[0]))

end = a[0][1]
cnt = 1
for i in range(1, n):
    start = a[i][0]
    if end <= start:
        end = a[i][1]
        cnt += 1
print(cnt)