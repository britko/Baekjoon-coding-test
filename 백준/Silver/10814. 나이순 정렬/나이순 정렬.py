import sys

input = sys.stdin.readline

n = int(input())

users = []
for _ in range(n):
    age, name = input().split()
    users.append((int(age), name))

users.sort(key=lambda x: x[0])

for i in range(n):
    print(*users[i])