# 10진수 -> 2진수
# 간단하게 python 내장 함수 bin() 사용 가능
# bin(20)의 경우 0b10100 형식으로 나오기 때문에 순수 2진수는 bin(20).[2:]

def binary(num):
  bin = ""
  while num > 0:
    bin += str(num % 2)
    num //= 2
  # return "".join(reversed(bin))
  return bin[::-1]

print(binary(20))