# lower 활용
def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')

# collections.Counter 활용
'''
from collections import Counter

def solution(s):
    counter = Counter(s)
    return (counter['p'] + counter['P']) == (counter['y'] + counter['Y'])
'''

# count 활용
'''
def solution(s):
    p_count = s.count('p') + s.count('P')
    y_count = s.count('y') + s.count('Y')
    return p_count == y_count
'''