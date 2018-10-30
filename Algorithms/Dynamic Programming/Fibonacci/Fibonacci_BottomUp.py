def fib_bup(N):
    fib_list = [0] * (N+1)
    if N > 0:
        fib_list[1] = 1
    for i in range(2, N+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[N]
