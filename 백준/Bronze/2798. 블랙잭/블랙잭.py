from itertools import permutations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

a = list(map(int, input().split()))

max_sum = 0
permutation = list(permutations(a, 3))

for i in permutation:
    if m >= sum(i):
        max_sum = max(max_sum, sum(i))

print(max_sum)