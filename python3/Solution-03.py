from functools import reduce
def factors(n):
	return sorted(list(set(reduce(list.__add__,([i,n//i] for i in range(1,int(n**0.5)+1) if n%i==0)))))
def isPrime(n):
	return len(factors(n))==2
l=factors(600851475143)
ll=[]
for i in l:
	if isPrime(i):
		ll.append(i)
print(max(ll))