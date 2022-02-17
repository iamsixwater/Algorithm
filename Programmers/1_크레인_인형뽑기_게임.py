def solution(board, moves):
    mvs = [n - 1 for n in moves]
    depth = len(board)
    stack = []
    answer = 0
    
    for m in mvs:
        for i in range(depth):
            if board[i][m] != 0:
                if len(stack) > 0 and stack[-1] == board[i][m]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(board[i][m])
                board[i][m] = 0
                break
                    
    return answer