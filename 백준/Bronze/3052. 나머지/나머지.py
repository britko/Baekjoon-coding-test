arr = [0 for _ in range(43)]    # 인덱스 1 ~ 42까지 배열 생성

for _ in range(10):
    n = int(input())
    mod = n % 42
    arr[mod] += 1   # 나머지 위치의 인덱스 +1
    
arr_mod = list(filter(lambda x : x > 0, arr))  # 나머지로 나온 수의 개수가 1개 이상인 원소 필터링

print(len(arr_mod))