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