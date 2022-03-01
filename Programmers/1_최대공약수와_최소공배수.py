def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer

def gcd(n, m):
    x = max(n, m)
    y = min(n, m)
    while y > 0:
        r = x % y
        if r == 0:
            return y
        x = y
        y = r
        
def lcm(n, m):
    return int(n * m / gcd(n, m))