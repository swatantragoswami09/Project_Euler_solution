import itertools
def compute():
    ans=max(range(1,1000), key=f)
    return ans
def f(n):
    s={}
    x=1
    for i in itertools.count():
        if x in s:
            return i-s[x]
        else:
            s[x]=i
            x=x*10%n
print(compute())