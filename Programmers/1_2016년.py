def solution(a, b):
    end_of_month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day_of_week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    days_from_start = sum([end_of_month[m] for m in range(1, a)]) + b
    return day_of_week[days_from_start % 7]