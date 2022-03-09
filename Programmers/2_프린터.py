# deque 활용
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

# tuple, any 사용
'''
def solution(properties, location):
    queue = [(i, q) for i, q in enumerate(properties)]
    answer = 0
    
    while True:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer
            
    return answer
'''