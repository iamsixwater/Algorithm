def solution(s):
    if s[0] == "-":
        return -1 * int(s[1:])
    return int(s)

# 함수 int(): 음/양 자동 인식
# def solution(s):
#     return int(s)