def compute():
    ans=sum(i for i in range(2,1000000) if i==fifth_digit_sum(i))
    print(ans)
def fifth_digit_sum(n):
     return sum(int(i)**5 for i in str(n))
compute()
