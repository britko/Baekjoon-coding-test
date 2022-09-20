import sys

input = sys.stdin.readline
n = int(input())

l, i = 1, 0
while True:
    l += 6 * i
    if n - l <= 0:
        break
    i += 1
    
print(i+1)