def fibonacci(N):
    fib_memo = [-1] * (N+1)
    return fibonacci_memo(N, fib_memo)

def fibonacci_memo(N, fib_memo):
    if N <= 1:
        return N
    elif fib_memo[N] != -1:
        return fib_memo[N]
    else:
        fib_memo[N] = fibonacci(N-1) + fibonacci(N-2)
        return fib_memo[N]

if __name__ == '__main__':
    print(fibonacci(5))
