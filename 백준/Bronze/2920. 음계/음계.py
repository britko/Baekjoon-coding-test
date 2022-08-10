x = list(map(int, input().split()))
a = [n for n in range(1, 9)]
d = [n for n in range(8, 0, -1)]

if x == a:
    print('ascending')
elif x == d:
    print('descending')
else:
    print('mixed')