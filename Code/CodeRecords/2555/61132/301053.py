def finstr(l,pre,Sum):
    if Sum==3:return 1
    if not l:return 0
    ans=0
    for i in range(len(l)):
        if l[i]>pre:
            ans+=finstr(l[i+1:],l[i],Sum+1)
    return ans

t=int(input())
l=list(map(int,input().split()))
print(finstr(l,min(l)-1,0),end='')