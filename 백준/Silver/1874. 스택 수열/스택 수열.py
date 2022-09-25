import sys

input = sys.stdin.readline
n = int(input())

stack = []
result = []
x = 1

for _ in range(n):
    num = int(input())
    while x <= num:
        stack.append(x)
        result.append('+')
        x += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        break
else:
    for i in result:
        print(i)