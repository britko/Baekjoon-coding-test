def solution(myString):
    
    return list(map(lambda x: len(x), list(myString.split('x'))))