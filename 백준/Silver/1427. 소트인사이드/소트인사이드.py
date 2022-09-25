n = input()

a = []
for c in n:
    a.append(c)
a.sort(reverse=True)

print(''.join(a))