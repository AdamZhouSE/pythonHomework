def mmgp(l,k_2):
    if k_2==0 or not l:return 0
    ans=[]
    for i in range(len(l)):
        ans.append((l[i] if k_2%2==1 else -l[i])+max(0,mmgp(l[i+1:],k_2-1)))
    return max(0,max(ans))

t = int(input())
for j in range(t):
    k=int(input())
    m=int(input())
    l=list(map(int,input().split()))
    print(mmgp(l,k*2))