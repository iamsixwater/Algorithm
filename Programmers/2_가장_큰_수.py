def solution(numbers):
    str_nums = list(map(str, numbers))
    str_nums.sort(key = lambda x: x * 3, reverse = True)
    return str(int("".join(str_nums)))

'''
1) lambda x: x * 3
숫자의 자릿수를 맞춰서 비교하기 위함
한 자리 숫자를 세 자리 숫자로 늘인 다음에 비교
[3, 31, 310]
333||
313||131
310||310310
=> [3, 31, 310]

2) str(int("".join()))
"0000"의 경우 0으로 만들어주기 위함
'''