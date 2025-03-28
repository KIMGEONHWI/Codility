def solution(X, Y, D):
    if (Y-X) % D == 0:
        return (Y-X) // D
    elif (Y-X) % D != 0:
        return ((Y-X) // D) + 1