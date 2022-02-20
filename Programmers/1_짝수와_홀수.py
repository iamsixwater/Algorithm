def solution(num):
    return "Odd" if num % 2 == 1 else "Even"

# def solution(num):
    # return ["Even", "Odd"][num & 1]
'''
<3>     <4>
 11     100
&01    &001
---    ----
 01     000
=> 2진수의 경우, 마지막 자리에 1이 있으면 홀수, 0이 있으면 짝수
'''
