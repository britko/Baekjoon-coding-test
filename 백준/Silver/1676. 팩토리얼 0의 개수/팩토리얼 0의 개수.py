import math

n = int(input())
fac_n = str(math.factorial(n))
cnt = 0

for i in range(len(fac_n) -1, 0, -1):
    if fac_n[i] == '0':
        cnt += 1
    else:
        break

print(cnt)