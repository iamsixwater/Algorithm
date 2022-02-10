def solution(lottos, win_nums):
    win_count = 0
    zero_count = 0
    
    for lotto in lottos:
        if lotto == 0: 
            zero_count += 1
        if lotto in win_nums:
            win_count += 1
    
    # 최고 당첨 개수: win_count + zero_count
    # 최저 당첨 개수: win_count
    # 7 - 당첨 개수: 순위(<= 6)
    answer = [0, 0]
    answer[0] = 7 - win_count - zero_count if 7 - win_count - zero_count <= 6 else 6
    answer[1] = 7 - win_count if 7 - win_count <= 6 else 6
    return answer
