# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    max_sum = A[0]
    current_sum = A[0]

    for i in range(1, len(A)):
        current_sum = max(A[i], current_sum + A[i])
        max_sum = max(current_sum, max_sum)
    return max_sum


