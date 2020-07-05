n = int(input())
for j in range(n):
    n = int(input())
    l=list(map(int,input().split()))
    ans=[]
    for i in range(len(l)-1):
        if l[i] >= max(l[i+1:]):
            ans.append(l[i])
    ans.append(l[-1])
    print(' '.join(map(str,ans)))