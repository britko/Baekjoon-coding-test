def solution(num_list):
    l, r = num_list[-2], num_list[-1]
    
    if r > l:
        num_list.append(r - l)
    else:
        num_list.append(r * 2)
    
    return num_list