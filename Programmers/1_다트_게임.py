def solution(dartResult):
    dart = list(dartResult)
    result = [0] * 3
    
    current_num = 0
    current_idx = -1 # 현재 몇 번째 다트 결과 계산 중인지
    for d in dart:
        if d.isdigit():
            current_num = current_num * 10 + int(d)
        elif d in ("S", "D", "T"):
            current_idx += 1
            result[current_idx] = cal_bonus(current_num, d)
            current_num = 0
        elif d == "*":
            result[current_idx] *= 2
            if current_idx > 0:
                result[current_idx - 1] *= 2
        elif d == "#":
            result[current_idx] *= -1
    
    return sum(result)

def cal_bonus(num, bonus):
    result = 0
    if bonus == "S":
        result = num
    elif bonus == "D":
        result = pow(num, 2)
    elif bonus == "T":
        result = pow(num, 3)
    
    return result