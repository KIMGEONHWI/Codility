def solution(A, B):
    stack = []
    survivors = 0

    for i in range(len(A)):
        size = A[i]
        direction = B[i]

        if direction == 1:
            stack.append(size)
        else:
            while stack:
                if stack[-1] > size:
                    break
                else:
                    stack.pop()
            else:
                survivors += 1

    return survivors + len(stack)
