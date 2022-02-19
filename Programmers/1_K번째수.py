def solution(array, commands):
    answer = []
    
    # for cmd in commands:
        # answer.append(sorted(array[cmd[0] - 1:cmd[1]])[cmd[2] - 1])
        
    for i, j, k in commands:
        answer.append(sorted(array[i - 1:j])[k - 1])
    
    return answer

'''
# lambda 인자리스트: 표현식
# map(함수, 인자)

def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))

'''