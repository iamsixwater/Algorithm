def solution(numbers, hand):
    # nums = [n - 1 for n in numbers]
    nums = [n - 1 if n > 0 else 10 for n in numbers] #if n == 0: n = 11
    answer = ""
    left = 9
    right = 11
    
    for num in nums:
        if num % 3 == 0:
            left = num
            answer += "L"
        elif num % 3 == 2:
            right = num
            answer += "R"
        else: # num % 3 == 1
            left_dist = cal_dist(num, left)
            right_dist = cal_dist(num, right)
            if left_dist < right_dist:
                left = num
                answer += "L"
            elif left_dist > right_dist:
                right = num
                answer += "R"
            else: # left_dist == right_dist:
                if hand == "left":
                    left = num
                    answer += "L"
                elif hand == "right":
                    right = num
                    answer += "R"
    
    return answer

def cal_dist(num1, num2):
    if abs(num1 - num2) % 3 == 0:
        return abs(num1 - num2) // 3
    return abs(num1 // 3 - num2 // 3) + 1

'''
0  1  2 -> n // 3 == 0
3  4  5 -> n // 3 == 1
6  7  8 -> n // 3 == 2
9 10 11 -> n // 3 == 3
'''