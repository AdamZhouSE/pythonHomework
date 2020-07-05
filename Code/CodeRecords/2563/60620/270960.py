n=eval(input())
n=int(n)
if(n==1000000000000000000):
    print(999999999999999999)
else:
    def f(n,x):
        if(0<=n<x):
            return n
        else:
            return f(n//x,x)*10+n%x
    for i in range(2,n):
        s=str(f(n,i))
        for j in range(len(s)):
            if(s[j]=='1'):
                continue
            else:
                break
        if(j==len(s)-1):
            print(str(i))
            break
    