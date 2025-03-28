# 44점 - 첫 시도
def solution(A):
    set_A = set(A)
    sort_set_A = sorted(set_A)

    plus_max = sort_set_A[-1] * sort_set_A[-2] * sort_set_A[-3]
    minus_max = sort_set_A[0] * sort_set_A[1] * sort_set_A[-1]

    if plus_max > minus_max:
        return plus_max
    else:
        return minus_max
    

## 100점 - 두번째 시도(중복되는 값 허용하는 것을 허용하기 때문에 set 사용하지 않고, 바로 오름차순 정렬)
def solution(A):
    A.sort()

    plus_max = A[-1] * A[-2] * A[-3]
    minus_max = A[0] * A[1] * A[-1]

    if plus_max > minus_max:
        return plus_max
    else:
        return minus_max