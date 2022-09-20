import sys

def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

input = sys.stdin.readline
n = int(input())

result = 0
for x in list(map(int, input().split())):
    if isprime(x):
        result += 1

print(result)