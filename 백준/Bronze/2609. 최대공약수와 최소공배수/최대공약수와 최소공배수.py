a, b = map(int, input().split())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    for i in range(max(x, y), x * y + 1):
        if i % a == 0 and i % b == 0:
            return i

print('%d\n%d'%(gcd(a, b), lcm(a, b)))