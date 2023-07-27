import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
id = dict()
name = dict()

for i in range(1, n + 1):
    pokemon = input()
    id[i] = pokemon
    name[pokemon] = i

for _ in range(m):
    x = input()
    
    if x.isdigit():
        print(id[int(x)])
    else:
        print(name[x])