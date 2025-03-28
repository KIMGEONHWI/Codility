def solution(H):
    stack = []
    blocks = 0

    for height in H:
        while stack and height < stack[-1]:
            stack.pop()

        if stack and stack[-1] == height:
            continue

        stack.append(height)
        blocks += 1

    return blocks
