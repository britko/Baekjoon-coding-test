n = input()

for i in range(int(n)+1):
    x = i
    for j in str(i):
        x += int(j)
    if x == int(n):
        print(i)
        break
    if i == int(n):
        print(0)