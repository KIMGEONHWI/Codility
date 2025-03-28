def solution(A):
    answer = 0
    sum_A = sum(A)

    for i in range(1, len(A) + 2):
        answer += i

    return answer - sum_A
