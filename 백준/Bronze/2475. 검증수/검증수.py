arr = list(map(int, input().split()))

def solution(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i] ** 2

    result = sum % 10

    return result

print(solution(arr))