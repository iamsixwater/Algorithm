def solution(name):
    answer = 0
    
    # name 꼬리에 A가 몇 개가 있나
    tail_a_len = 0
    for i in range(len(name) - 1, -1, -1):
        if name[i] != 'A':
            break
        tail_a_len += 1
    if tail_a_len == len(name):
        return answer
    
    # 왼쪽에서 오른쪽으로 한 방향으로 진행했을 때 이동 거리
    min_length = len(name) - 1 - tail_a_len
    
    # 조이스틱 조작 횟수 계산
    min_move = min_length # 좌우 최소 이동 거리
    for i, n in enumerate(name):
        # prev, next
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
        
        # left, right
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min([min_move, i * 2 + len(name) - next, i + (len(name) - next) * 2])
        # i: A가 아닌 위치까지 전진
        # len(name) - next: 맨 뒤에서부터 앞으로 A가 아닌 위치까지 전진
        # min([min_move, 오른쪽 방향으로 왕복, 왼쪽 방향으로 가장 뒤부터 왕복])

    answer += min_move
    
    return answer