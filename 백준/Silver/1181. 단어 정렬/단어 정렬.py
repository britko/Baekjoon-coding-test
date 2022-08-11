n = int(input())

# 중복 단어 제거를 위해 set에 입력값 추가
arr_s = set()

for _ in range(n):
    s = input()
    arr_s.add(s)

# 정렬을 위해 리스트로 변환
arr_l = list(arr_s)

arr_l.sort()    # 사전 순으로 정렬
arr_l.sort(key=lambda x: len(x))    # 길이 순으로 정렬

for i in range(len(arr_l)):
    print(arr_l[i])