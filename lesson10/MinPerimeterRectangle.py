#첫번째 - 50점
import math

def solution(N):
    data = []
    y = 0
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            data.append(i)
        else:
            pass
    

    for i in range(1, N+1):
        if data[-1] * i == N:
            y = i
    return (data[-1] + y) * 2

#두번째 - 100점
import math

def solution(N):
    min_perimeter = float('inf')

    for A in range(1, int(math.sqrt(N)) + 1):
        if N % A == 0:
            B = N // A
            perimeter = 2 * (A + B)
            min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter
