def find(x,y,z):
    if(z>x+y):
        return False
    if(z==x or z==y or z==x+y):
        return True
    if(x==0 or y==0):
        return False
    gcd=1
    n=max(x,y)
    m=min(x,y)
    for i in range(2,m+1):
        if(m%i==0 and n%i==0):
            gcd=i
    return(z%gcd==0)
        
x=eval(input())
y=eval(input())
z=eval(input())
print(find(x,y,z))