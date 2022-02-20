def solution(N, stages):
    completed = {}
    for n in range(1, N + 2):
        completed[n] = 0
    
    total_user = 0
    for stage in stages:
        completed[stage] += 1
        total_user += 1
        
    for stage, c in completed.items():
        if c == 0:
            continue
        completed[stage] /= total_user
        total_user -= c
        
    # 실패율 높은 순으로 정렬
    print(completed)
    sorted_dict = sorted(completed.items(), reverse = True, key = lambda item: item[1])
    
    answer = []
    for n in range(0, N + 1):
        if sorted_dict[n][0] < N + 1:
            answer.append(sorted_dict[n][0])
    
    return answer