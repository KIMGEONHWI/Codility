def solution(N, A):
    counters = [0] * N
    max_counter = 0      
    last_update = 0     

    for op in A:
        if 1 <= op <= N:
            if counters[op - 1] < last_update:
                counters[op - 1] = last_update

            counters[op - 1] += 1

            if counters[op - 1] > max_counter:
                max_counter = counters[op - 1]

        elif op == N + 1:
            last_update = max_counter 
    for i in range(N):
        if counters[i] < last_update:
            counters[i] = last_update

    return counters
