def solution(n, _lost, _reserve):
    lost = [x for x in _lost if x not in _reserve]
    reserve = [x for x in _reserve if x not in _lost]
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            answer += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            answer += 1
        
    return answer