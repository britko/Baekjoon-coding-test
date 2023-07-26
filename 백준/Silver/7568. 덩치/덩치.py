n = int(input())
specs = list()
for _ in range(n):
    w, h = map(int, input().split())
    specs.append([w, h, 1])

for i in range(n):
    for j in range(n):
        if specs[i][0] < specs[j][0] and specs[i][1] < specs[j][1]:
            specs[i][2] += 1

for i in range(n):
    print(specs[i][2], end=' ')