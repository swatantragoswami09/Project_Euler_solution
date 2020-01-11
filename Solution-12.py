import itertools
from functools import reduce
def ss():
	t=0
	for i in itertools.count(1):
		t+=i
		if len(factor(t))>500:
			return str(t)
def factor(n):
	return set(reduce(list.__add__,([i,n//i] for i in range(1,int(n**0.5)+1) if n%i==0)))
print(ss())