arr = [x for x in range(1, 31)]

for _ in range(28):
    x = int(input())
    arr.remove(x)

for i in range(2):
    print(arr[i])