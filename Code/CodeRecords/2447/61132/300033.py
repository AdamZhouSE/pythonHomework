m,k=map(int,input().split())
l=list(map(int,input().split()))
ans=[]
for j in range(k):
    n1,n2=map(int,input().split())
    ans.append(min(l[n1-1:n2]))
print(' '.join(map(str,ans)),end='')