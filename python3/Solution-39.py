def compute():
    ans=max(range(1,1001),key=count_solutions)
    return ans
def count_solutions(p):
    result=0
    for i in range(1,p+1):
        for j in range(i,(p-i)//2+1):
            c=p-i-j
            if i*i+j*j==c*c:
                result+=1
    return result
print(compute())
