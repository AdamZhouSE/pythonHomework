def find(a):
    result=10
    f=9
    if(a==1): return(10)
    if(a==0): return(0)
    else:
        for i in range(2,a+1):
            f*=(10-i+1)
            result+=f
    return result

a=eval(input())
print(find(a))
