p,n=input().split()
p,n=int(p),int(n)
result=0
s=""
while n>0:
    n -= 1
    x=int(input())
    mod=str(x%p)+" "
    if (s.find(mod)==-1):
        s=s+mod
        result +=1
    else:
        print(result+1)
        break
if n==0:
    print(-1)