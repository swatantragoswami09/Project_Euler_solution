c=0
def f(n):
	global c
	if n==1:
		return 1
	elif n%2==0:
		y=n//2
	elif n%2!=0:
		c+=1
		# print(n,end=' ')
		y=3*n+1
	return f(y)+1

ans=max(range(1,1000000),key=f)
print(ans)