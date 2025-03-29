#첫번째 - 35점
import math

def solution(N):
    data = []
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            data.append(i)
        else:
            pass
    return len(data)*2


#두번째 - 100점
import math

def solution(N):
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i * i == N:
                count += 1
            else:
                count += 2
    return count

