def fibonacci(n):
    if n < 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)

# Non-memoized version
# %timeit fibonacci(20)
# 3.95 ms ± 153 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)