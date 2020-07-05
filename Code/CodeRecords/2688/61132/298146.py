def substr(l,prefix,Sum):
    if not l or prefix>=Sum:return [prefix]
    ans=[]
    for i in range(len(l)):
        ans+=substr(l[i+1:],prefix+l[i],Sum)
    ans=[i for i in ans if i ==Sum]
    return ans
t = int(input())
for j in range(t):
    k=int(input())
    l=list(map(int,input().split()))
    Sum=int(input())
    print(len(substr(l,0,Sum)))