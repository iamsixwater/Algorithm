from math import ceil

def solution(progresses, speeds):
    time = []
    for p, s in zip(progresses, speeds):
        time.append(ceil((100 - p) / s))
    
    answer = []
    max_days = time[0]
    deploy = 0
    for i in range(len(time)):
        if max_days >= time[i]:
            deploy += 1
        else:
            answer.append(deploy)
            deploy = 1
            max_days = time[i]
    answer.append(deploy)
    
    return answer