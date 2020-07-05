def f(n):
    if(n==1):
        return '1'
    if(n%2==0):
        return f(int(n/2))+'0'
    return f(int(n/2))+'1'

t=int(input())
for i in range(t):
    n=int(input())
    s=f(n)
    c=0;ind=-1
    for i in range(1,len(s)+1):
        if(s[-i]=='1'):
            c+=1
            if(c>1):
                ind=-1
                break
            else:
                ind=i
    print(ind)