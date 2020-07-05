def double(n):
    a=n
    while a>0:
        a=a//2
        if a%2!=0:
            return False
    return True
def need(n):
    if double(n):
        return 1
    elif n%2==1:
        return 1+need(n-1)
    else:
        n1=n//2
        return need(n1)
        
    
num=int(input())
for k in range(num):
    n=int(input())
    print(need(n))
    
    