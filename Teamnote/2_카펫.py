def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            if brown == ((i + 1) * 2 + (yellow//i + 1) * 2):
                answer.append(yellow // i + 2)
                answer.append(i + 2)
    
    return answer