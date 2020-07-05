def f(a):
    if a<=4:
        return 0
    elif 10>a>=5:
        return 1
    elif a==10:
        return 2
    else:
        k=1
        S=5
        s=0
        while S<a:
            S*=5
            k+=1
        for i in range(1,k+1):
            n=5
            for j in range(1,i):
                n*=5
            s+=a-int(a/n)
            
        return s
    
    
print(f(int(input().strip())))