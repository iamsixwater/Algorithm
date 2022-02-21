# 대칭 이용: n // 2, sqrt(n)
# 대칭 이용 이유: n = a * b: 약수를 구하면 그 짝이 되는 수가 항상 존재한다. ex> 12 = 3 * 4
# 두 수를 곱해서 n을 넘지 않으려면 sqrt(n)를 기점으로 양 옆 두 수를 곱하면 된다.
# sqrt(n)를 기점으로 그 전 수까지 곱해서 충분히 n을 도출할 수 있다.

def solution(n):
    nums = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            nums.append(i)
            if i ** 2 != n: # n = a * a 인 케이스 중복 방지: ex> 25 = 5 * 5
                nums.append(n / i)
            
    return sum(nums)

# def solution(n):
#     aliquot = []
    
#     for i in range(1, n + 1):
#         if n % i == 0:
#             aliquot.append(i)
    
#     return sum(aliquot)