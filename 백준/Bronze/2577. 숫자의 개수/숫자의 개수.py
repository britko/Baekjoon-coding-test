nums = [0 for x in range(10)]
a = list()

mul = 1

for _ in range(3):
    mul *= int(input())

str_mul = str(mul)

for i in str_mul:
    nums[int(i)] += 1

for i in nums:
    print(i)