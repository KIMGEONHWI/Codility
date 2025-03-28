def solution(X, A):
    positions = set()
    
    for time, leaf in enumerate(A):
        if 1 <= leaf <= X:
            positions.add(leaf)
        if len(positions) == X:
            return time

    return -1