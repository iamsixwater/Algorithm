def solution(absolutes, signs):
    answer = 0
    
    for idx, num in enumerate(absolutes):
        answer += num if signs[idx] else -num
            
    return answer

# zip 활용
'''
def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))
'''