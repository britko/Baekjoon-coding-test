h, m = map(int, input().split())

ch_m = m - 45

if ch_m < 0 and h != 0:
    h -= 1
    m = 60 + ch_m
elif ch_m < 0 and h == 0:
    h = 23
    m = 60 + ch_m
else:
    m = m - 45
    
print(h, m)