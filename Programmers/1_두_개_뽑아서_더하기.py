def solution(numbers):
    answer = []
    
    for idx, i in enumerate(numbers):
        for j in numbers[idx + 1:]:
            answer.append(i + j)
    
    return sorted(list(set(answer)))

# combination 사용
'''
from itertools import combinations

def solution(numbers):
    combs = list(combinations(numbers, 2))
    
    answer = []
    for c in combs:
        answer.append(c[0] + c[1])
    
    return sorted(list(set(answer)))
'''