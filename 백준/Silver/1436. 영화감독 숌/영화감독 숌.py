n = int(input())
a = []

for i in range(2700000):
    if '666' in str(i):
        a.append(i)
    if len(a) == n:
        print(i)
        break