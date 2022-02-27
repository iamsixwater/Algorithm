# 기존 풀이
def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        if cal_aliquot_num(num) % 2 == 0:
            answer += num
        else:
            answer -= num
            
    return answer

def cal_aliquot_num(num):
    count = 0
    
    for n in range(1, int(num ** 0.5) + 1):
        if num % n  == 0:
            count += 2
            if n ** 2 == num:
                count -= 1
    
    return count

# 제곱 수의 약수 개수는 홀수라는 것 이용
'''
def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        if (num ** 0.5) == int(num ** 0.5):
            answer -= num
        else:
            answer += num
    
    return answer
'''