'''
소수(prime number) 구하기
에라토스테네스의 체 활용
시간 복잡도: O(NloglogN)
'''
def make_sieve(max_num):
  MAX = max_num + 1
  sieve = [0] * 2 + [1] * (MAX - 2)
  for i in range(2, int(MAX ** 0.5) + 1):
    if sieve[i] != 0:
      for j in range(i + i, MAX, i):
        sieve[j] = 0
  return sieve

print(make_sieve(100))