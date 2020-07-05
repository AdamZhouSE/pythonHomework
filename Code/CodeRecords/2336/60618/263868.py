t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=[int(n) for n in input().split()]
    re=''
    for j in range(0,n-k+1):
        re+=' '+str(max(a[j:j+k]))
    print(re[1:])
        