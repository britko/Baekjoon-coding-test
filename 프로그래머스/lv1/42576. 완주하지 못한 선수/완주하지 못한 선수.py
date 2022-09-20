def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("_")
    for i in range(0, len(completion)):
        if(participant[i] != completion[i]):
            answer = participant[i]
            break
    return answer