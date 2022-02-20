# 단일 반복문으로 실행 시간 짧음 O(n)
'''
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
'''

# 이중 반복분으로 실행 시간 오래 걸림 O(n^2)
def solution(N, stages):
    result = {}
    total_user = len(stages)
    
    for n in range(1, N + 1):
        if total_user > 0:
            n_count = stages.count(n) # O(n)
            result[n] = n_count / total_user
            total_user -= n_count
        else:
            result[n] = 0
    
    return sorted(result, key = lambda x: result[x], reverse = True)

'''
# sorted
result => result.keys()랑 같은 뜻(keys 생략 가능)
key => 정렬을 목적으로 하는 함수(lambda 이용 가능)
lambda x: result[x] => result[key]가 되므로, value를 기준으로 정렬하겠다는 의미
'''
    