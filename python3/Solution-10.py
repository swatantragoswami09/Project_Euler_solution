from functools import reduce
def factor(n):
	return list(set(reduce(list.__add__,([i,n//i] for i in range(1,int(n**0.5)+1) if n%i==0))))
def isPrime(n):
	l1=[]
	for i in range(2,n):
		if len(factor(i))==2:
			l1.append(i)
	return sum(l1)
print(isPrime(2000000))
