import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = list(sys.stdin.readline().split())
    for i in range(len(s)):
        s[i] = s[i][::-1]
    print(' '.join(s))