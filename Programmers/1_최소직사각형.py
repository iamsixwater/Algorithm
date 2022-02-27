def solution(sizes):
    min_size = 1001
    max_size = 0
    
    for idx, size in enumerate(sizes):
        if idx == 0:
            min_size = min(size[0], size[1])
            max_size = max(size[0], size[1])
        else:
            min_size = max(min_size, min(size[0], size[1]))
            max_size = max(max_size, max(size[0], size[1]))
    
    return min_size * max_size
