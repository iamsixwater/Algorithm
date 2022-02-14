def solution(s):
    number_list = ["zero", "one", "two", "three", "four", "five",
                  "six", "seven", "eight", "nine"]
    answer = ""
    str_num = ""
    
    for c in s:
        if c.isdigit():
            answer += str(c)
        else:
            str_num += c
            if str_num in number_list:
                answer += str(number_list.index(str_num))
                str_num = ""
    
    return int(answer)

# replace 사용 버전
'''
def solution(s):
    number_map = {
        "zero": 0, "one": 1, "two": 2, "three": 3,
        "four": 4, "five": 5, "six": 6, "seven": 7,
        "eight": 8, "nine": 9
    }
    
    for key, value in number_map.items():
        s = s.replace(key, str(value))
    
    return int(s)
'''