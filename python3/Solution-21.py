def compute():
    d=[0]*10000
    for i in range(1,len(d)):
        for j in range(i*2,len(d),i):
            d[j]+=i
    ans=0
    for i in range(1,len(d)):
        j=d[i]
        if j!=i and j<len(d) and d[j]==i:
            ans+=i
    return ans
print(compute())