for i in range(1,1001):
    for j in range(1,1001):
        c=1000-(i+j)
        if i**2+j**2==c**2:
            print(i*j*c)
                
