def solution(s):
    return s[int(len(s) / 2) - ((len(s) + 1) % 2) : int(len(s) / 2) + 1]
    # return s[(len(s) - 1) // 2 : len(s) // 2 + 1]
s