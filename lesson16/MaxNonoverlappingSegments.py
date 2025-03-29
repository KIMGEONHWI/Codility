def solution(A, B):
    N = len(A)
    count = 0
    last_end = -1

    for i in range(N):
        if A[i] > last_end:
            count += 1
            last_end = B[i]

    return count