from collections import Counter

s = input().upper()

cnt = Counter(s)
    
max_ap = dict(filter(lambda e: e[1] == max(cnt.values()), cnt.items()))

if len(max_ap) == 1:
    print(list(max_ap.keys())[0])
else:
    print('?')