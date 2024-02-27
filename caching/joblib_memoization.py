from joblib import Memory

cachedir='/jobcache'
memory = Memory(cachedir)

@memory.cache
def sum(a, b):
    return a + b