import fractions
ans=1
for i in range(1,21):
    ans=ans*i//fractions.gcd(i,ans)
print(ans)
