def solution(arr):
    answer = []
    num = -1
    for a in arr:
        if a == num:
            continue
        answer.append(a)
        num = a
        
    return answer

# slicing 활용
'''
def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0 or a != answer[-1]:
            answer.append(a)
    
    return answer
'''