t=int(input())
for i in range(t):
    n,l,r=map(int,input().split())
    a=list(bin(n))
    a.remove(a[0])
    a.remove(a[0])
    for j in range(len(a)-r,len(a)-l+1):
        if(a[j]=='0'):
            a[j]='1'
    result=''.join(a)
    print(int(result,2))
    
    