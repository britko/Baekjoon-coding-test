n, k = map(int, input().split())

arr = [x + 1 for x in range(n)]

print('<', end='')

cnt = 0
while arr:
    cnt += 1
    if cnt % k == 0:
        if len(arr) > 1:
            print(arr.pop(0), end=', ')
        else:
            print(arr.pop(0), end='')
    else:
        x = arr.pop(0)
        arr.append(x)

print('>')