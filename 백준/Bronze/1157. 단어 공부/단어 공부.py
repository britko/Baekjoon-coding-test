s = input().upper()

d = dict()

for x in s:
    d[x] = 0

for x in s:
    d[x] += 1
    
max_ap = dict(filter(lambda e: e[1] == max(d.values()), d.items()))

if len(max_ap) == 1:
    print(list(max_ap.keys())[0])
else:
    print('?')