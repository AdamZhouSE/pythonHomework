def mmgp(l,k_2):
    if k_2==0 or not l:return 0
    ans=[]
    for i in range(len(l)):
        ans.append(mmgp(l[i+1:],k_2-1)
    return (l[i] if k_2%2==1 else -l[i])+max(0,ans)

t = int(input())
for j in range(t):
    k=int(input())
    m=int(input())
    l=list(map(int,input().split()))
    print(mmgp(l,k*2,0))
    ans=mmgp(l,k*2,0)