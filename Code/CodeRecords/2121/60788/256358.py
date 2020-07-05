def f(n):
    s=0
    for i in range(1,n+1):
        s+=A(i)
    return s    
def A(i):
    if i==1:
        return 10
    elif i==2:
        return 81
    else:
        return A(i-1)*(11-i)
        
        

    
print(f(int(input().strip())))   