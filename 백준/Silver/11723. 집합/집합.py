import sys

input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    op = list(input().split())
    if op[0] not in ["all", "empty"]:
        x = int(op[1])

    if op[0] == "add":
        s.add(x)
    elif op[0] == "remove":
        s.discard(x)
    elif op[0] == "check":
        print(1 if x in s else 0)
    elif op[0] == "toggle":
        s.remove(x) if x in s else s.add(x)
    elif op[0] == "all":
        s = {i for i in range(1, 21)}
    elif op[0] == "empty":
        s = set()