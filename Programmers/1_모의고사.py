def solution(answers):
    correct = [0] * 3
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    
    for i, n in enumerate(answers):
        if n == first[i % len(first)]:
            correct[0] += 1
        if n == second[i % len(second)]:
            correct[1] += 1
        if n == third[i % len(third)]:
            correct[2] += 1
    
    max_correct = max(correct)
    for i, c in enumerate(correct):
        if c == max_correct:
            answer.append(i + 1)
    
    return answer