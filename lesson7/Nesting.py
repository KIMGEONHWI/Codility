def solution(S):
    stack = []

    for i in S:
        if len(stack) == 0:
            stack.append(i)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            stack.pop()
    return 1 if not stack else 0
