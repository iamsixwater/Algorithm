def solution(numbers):
    str_nums = list(map(str, numbers))
    str_nums.sort(key = lambda x: x * 3, reverse = True)
    return str(int("".join(str_nums)))

'''
1) lambda x: x * 3
* 3은 31, 310의 두 번째 자리 수인 1보다 먼저 나와야 함.
* 31의 1은 310의 세 번째 자리 수인 0보다 먼저 나와야 함.

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