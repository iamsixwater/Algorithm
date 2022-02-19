def solution(n):
    
    # 3진법 계산
    reversed_ternary = ""
    while n >= 3:
        reversed_ternary += str(n % 3)
        n //= 3
    reversed_ternary += str(n)
    
    answer = 0
    for idx, t in enumerate(reversed_ternary):
        if t != "0":
            answer += int(t) * 3 ** (len(reversed_ternary) - idx - 1)
    
    # int-base 사용 버전
    # answer = int(reversed_ternary, 3)        
    
    return answer