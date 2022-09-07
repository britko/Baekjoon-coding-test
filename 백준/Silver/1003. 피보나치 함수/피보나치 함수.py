t = int(input())

for _ in range(t):
    n = int(input())

    # DP 테이블 초기화(a: 0, b: 1)
    a = [0] * 41
    b = [0] * 41

    a[0], a[1], a[2] = 1, 0, 1
    b[1], b[2] = 1, 1

    for i in range(3, n+1):
        a[i] = a[i-1] + a[i-2]
        b[i] = b[i-1] + b[i-2]

    print(a[n], b[n])