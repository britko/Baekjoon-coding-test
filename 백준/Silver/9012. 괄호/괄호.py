import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stack = []
    s = input()

    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)

    print('YES' if len(stack) == 0 else 'NO')