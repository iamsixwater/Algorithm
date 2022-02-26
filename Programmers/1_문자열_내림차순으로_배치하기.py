def solution(s):
    characters = list(s)
    characters.sort(reverse = True)
    answer = "".join(characters)
    return answer