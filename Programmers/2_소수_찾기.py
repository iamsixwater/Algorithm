from itertools import permutations

def solution(numbers):
    MAX = 10000000
    sieve = [0] * 2 + [1] * (MAX - 2)
    for i in range(2, int(MAX ** 0.5) + 1):
        if sieve[i] != 0:
            for j in range(i + i, MAX, i):
                sieve[j] = 0
                
    num_set = set()
    for length in range(1, len(numbers) + 1):
        num_set.update(list(map(int, map("".join, permutations(numbers, length)))))
    
    answer = 0
    for num in num_set:
        if sieve[num] != 0:
            answer += 1
            
    return answer