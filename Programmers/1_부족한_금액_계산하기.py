def solution(price, money, count):
    prices = 0
    for c in range(1, count + 1):
        prices += price * c

    return 0 if money - prices >= 0 else prices - money