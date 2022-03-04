def solution(people, limit):
    people.sort(reverse = True)
    
    answer = 0
    l = 0
    r = len(people) - 1
    while l <= r:
        answer += 1
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            l += 1
    
    return answer