import itertools
def f():
    arr=list(range(3))
    temp=itertools.islice(itertools.permutations(arr),2,None)
    return ''.join(str(i) for i in next(temp))
print(f())