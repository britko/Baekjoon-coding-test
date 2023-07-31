import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

domains = {}

for _ in range(n):
    d, p = input().split()
    domains[d] = p

for _ in range(m):
    domain = input()
    print(domains[domain])