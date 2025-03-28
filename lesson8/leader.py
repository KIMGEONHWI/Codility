def solution(A):
    size = 0
    candidate = None

    for value in A:
        if size == 0:
            candidate = value
            size += 1
        elif candidate == value:
            size += 1
        else:
            size -= 1

    if A.count(candidate) > len(A) // 2:
        for i in range(len(A)):
            if A[i] == candidate:
                return i
    else:
        return -1