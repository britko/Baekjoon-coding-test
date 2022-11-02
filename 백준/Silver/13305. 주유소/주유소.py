n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

min = oil[0]
sum = 0

for i in range(n-1):
    if min > oil[i]:
        min = oil[i]
    sum += min * road[i]

print(sum)