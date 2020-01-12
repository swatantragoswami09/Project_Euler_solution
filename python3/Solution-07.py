from functools import reduce
def factors(n):
	return sorted(list(set(reduce(list.__add__,([i,n//i] for i in range(1,int(n**0.5)+1) if n%i==0)))))
def isPrime(n):
	return len(factors(n))==2

def n_prime(n):
	i=2
	while n>0:
		if isPrime(i):
			n=n-1
			if n==0:
				return i
		i=i+1
	return -1
print(n_prime(10001))