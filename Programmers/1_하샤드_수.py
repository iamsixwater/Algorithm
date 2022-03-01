def solution(x):
    num_sum = sum(map(int, list(str(x))))
    # return True if x % num_sum == 0 else False
    return x % num_sum == 0