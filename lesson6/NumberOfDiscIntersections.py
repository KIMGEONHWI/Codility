def solution(A):
    N = len(A)
    start = [i - A[i] for i in range(N)]
    end = [i + A[i] for i in range(N)]

    start.sort()
    end.sort()

    intersections = 0
    open_discs = 0
    j = 0

    for i in range(N):
        while j < N and start[j] <= end[i]:
            open_discs += 1
            j += 1

        intersections += open_discs - i - 1

        if intersections > 10_000_000:
            return -1

    return intersections
