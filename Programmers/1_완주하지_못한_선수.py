def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    athlete = ""
    completion_length = len(completion)
    for i in range(0, completion_length):
        if participant[i] != completion[i]:
            athlete = participant[i]
            break
    
    return athlete if athlete != "" else participant[completion_length]

'''
# 효율성 테스트 실패
# remove: O(n)

def solution(participant, completion):
    for c in completion:
        participant.remove(c)
    
    return participant[0]
'''