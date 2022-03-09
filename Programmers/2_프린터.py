from collections import deque

def solution(priorities, location):
    count = 0
    queue = deque(priorities)
    
    while True:
        if queue[0] >= max(queue):
            count += 1
            queue.popleft()
            if location == 0:
                return count
            location -= 1
            
        else:
            queue.append(queue[0])
            queue.popleft()
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
    
    return count