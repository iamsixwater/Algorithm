def solution(n, arr1, arr2):
    arr1_bin = [list(binary(x, n)) for x in arr1]
    arr2_bin = [list(binary(x, n)) for x in arr2]
    # bin(5|2) == 101|10 == 111로 변경 가능
    arr_bin = [[int(c) | int(d) for c, d in zip(a, b)] for a, b in zip(arr1_bin, arr2_bin)]
    
    answer = []
    for arr in arr_bin:
        tmp = ""
        for a in arr:
            if a == 1:
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)
    return answer

# python 내장 함수 bin() 존재
def binary(num, n):
    bin = ""
    while num > 0:
        bin += str(num % 2)
        num //= 2
    
    return "0" * (n - len(bin)) + bin[::-1]