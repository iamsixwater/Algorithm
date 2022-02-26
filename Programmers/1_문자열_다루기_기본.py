def solution(s):
    # return True if (len(s) == 4 or len(s) == 6) and s.isnumeric() else False
    return len(s) in (4, 6) and s.isnumeric()