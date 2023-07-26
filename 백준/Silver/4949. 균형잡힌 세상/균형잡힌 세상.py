while True:
    stack = []
    s = input()

    if s == '.':
        break

    if s[-1] != '.':
        print("no")
        continue

    for c in s:
        if c in ['(', '[']:
            stack.append(c)
        elif c == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
                break
        elif c == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")