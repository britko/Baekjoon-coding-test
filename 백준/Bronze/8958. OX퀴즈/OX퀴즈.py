n = int(input())

for _ in range(n):
    x = input()
    cnt = 0
    sum = 0
    for i in range(len(x)):
        if x[i] == 'O':
            cnt += 1
            sum += int(cnt)
        else:
            cnt = 0
    print(sum)