# gcd
'''
> 유클리드 호제법
자연수 a, b (단, a > b)
r = a % b
GCD(a, b) = GCD(b, r)
r이 0이면 그 때의 b가 최대공약수이다.
시간복잡도: O(logN)
'''
def gcd(a, b):
  x = max(a, b)
  y = min(a, b)
  while y > 0:
    r = x % y
    if r == 0:
      return y
    x = y
    y = r

# lcm
def lcm(a, b):
  return int(a * b / gcd(a, b))

print(gcd(24, 27))
print(lcm(24, 27))

