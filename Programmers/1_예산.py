def solution(d, budget):
    d.sort()
    
    answer = 0
    for num in d:
        if budget - num >= 0:
            answer += 1
            budget -= num
    
    return answer