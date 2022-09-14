def solution(answers):
    n = len(answers)
    a = [1, 2, 3, 4, 5] * (n // 5 + 1)
    b = [2, 1, 2, 3, 2, 4, 2, 5] * (n // 5 + 1)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (n // 5 + 1)
    cnt = [0, 0, 0]
    
    for i in range(n):
        if answers[i] == a[i]:
            cnt[0] += 1
        if answers[i] == b[i]:
            cnt[1] += 1
        if answers[i] == c[i]:
            cnt[2] += 1
        
    answer = [i+1 for i, x in enumerate(cnt) if x == max(cnt)]
    return answer