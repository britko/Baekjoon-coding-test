import sys

input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
i, j = 0, 0
psum = a[0]
result = n + 1

while True:
    if psum >= s:
        psum -= a[i]
        result = min(result, j - i + 1)
        i += 1
    else:
        j += 1
        if j >= n:
            break
        psum += a[j]

print(0) if result == n + 1 else print(result)