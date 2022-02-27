from itertools import combinations

def solution(nums):
    sieve = make_sieve(1000 * 3)
    combs = list(combinations(nums, 3))
    answer = 0
    
    for c in combs:
        # num = c[0] + c[1] + c[2]
        num = sum(c)
        if sieve[num] != 0:
            answer += 1
    
    return answer

def make_sieve(nums):
    sieve = [n for n in range(nums + 1)]
    for i in range(2, nums + 1):
        if sieve[i] != 0:
            for j in range(i + i, nums + 1, i):
                sieve[j] = 0
    return sieve