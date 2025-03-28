def solution(A, K):
    if not A:
        return A

    N = len(A)
    K = K % N 

    result = [0] * N
    for i in range(N):
        new_index = (i + K) % N
        result[new_index] = A[i]

    return result
