## 83점(sum으로만 순열 판단하면 부분 점수밖에 못 받는다)
def solution(A):
    A.sort()
    end_element = A[-1]
    if sum(A) == end_element * (end_element + 1) // 2:
        return 1
    else:
        return 0


## 100점
def solution(A):
    return int(len(A) == len(set(A)) and max(A) == len(A))
