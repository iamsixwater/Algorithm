def solution(n):
    sieve = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if sieve[i] != 0:
            for j in range(i + i, n + 1, i):
                sieve[j] = 0
                
    answer = 0
    for i in range(2, n + 1):
        if sieve[i] != 0:
            answer += 1
            
    return answer