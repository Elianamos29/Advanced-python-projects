import timeit

setup_code = '''
from functools import lru_cache
from fibonacci import fibonacci
fibonacci_memoized = lru_cache(maxsize=None) (fibonacci)
'''

results = timeit.repeat('fibonacci_memoized(20)',
                        setup=setup_code,
                        repeat=1000,
                        number=1)

print("fibonacci took {:.4f} us".format(min(results)))
# output: fibonacci took 0.0036 us