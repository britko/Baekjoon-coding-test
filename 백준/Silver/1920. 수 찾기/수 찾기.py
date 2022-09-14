n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()    # 이분 탐색을 위한 정렬

for target in b:
    result = 0  # 결과 저장(1: 존재, 0: 존재하지 않음)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            result = 1
            break
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(result)