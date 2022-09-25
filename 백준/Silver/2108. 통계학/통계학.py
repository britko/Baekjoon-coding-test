from collections import Counter
from statistics import mean
import sys

input = sys.stdin.readline
n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))
a.sort()

count = Counter(a).most_common(2)

print(round(mean(a)))
print(a[n//2])
if len(count) == 1 or count[0][1] != count[1][1]:
    print(count[0][0])
else:
    print(count[1][0])
print(a[-1] - a[0])