n = int(input())

money = 1000 - n
changes = [500, 100, 50, 10, 5, 1]
result = 0

for change in changes:
    result += money // change
    money = money % change
    if money == 0:
        break
print(result)