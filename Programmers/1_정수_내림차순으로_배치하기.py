def solution(n):
    nums = list(str(int(n)))
    nums.sort(reverse = True)
    return int("".join(nums))