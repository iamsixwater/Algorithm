# (n - 1)의 약수 중에 1을 제외한 가장 작은 수
# 1이 제외되는 이유는 1로 나누면 나머지가 1이 아니라 무조건 0이 나오기 때문에

def solution(n):
    for i in range(2, n):
        if (n - 1) % i == 0:
            return i
    