def get_max(a,b):
    if int(a+b)>int(b+a):
        return a
    else:
        return b
    

def sorting():
    N=int(input())
    a=list(input().split())
    a.sort()
    if N==0 or a[0]=='0':
        return '0'
    
    for i in range(0,N-1):
        for j in range (i+1,N):
            if get_max(a[i],a[j])==a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    s=''
    for e in a:
        s+=e
    return s


T=int(input())
for j in range(0,T):
    print(sorting())