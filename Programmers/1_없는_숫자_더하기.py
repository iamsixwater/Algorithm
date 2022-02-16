def solution(numbers):
    all_nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    original_nums = set(numbers)
    sub_nums = all_nums - original_nums
    
    answer = sum(list(sub_nums))
    return answer

# 모든 원소는 서로 다르다는 조건 확인 후
'''
def solution(numbers):
    answer = sum([i for i in range(10)]) - sum(numbers)
    return answer
'''