#50점 - 첫번째 시도(O(N**2))

def solution(A):
    answer = 0 
    for i in range(len(A)):
        if A[i] == 0:
            answer += A[i+1:].count(1)
    return answer

# 100점 - 두번째 시도(누적합 방식 사용, O(N))

def solution(A):
    east = 0
    pairs = 0

    for car in A:
        if car == 0:
            east += 1
        else:
            pairs += east  # 지금까지 본 동쪽 차들 수만큼 교차 발생

        if pairs > 1_000_000_000:
            return -1

    return pairs
