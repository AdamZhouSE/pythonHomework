def finstr(l,pre,Sum):
    if not l:return Sum
    ans=[]
    for i in range(len(l)):
        if l[i]>=pre:
            ans.append(finstr(l[i+1:],l[i],Sum+1))
    if not ans:return Sum
    return max(ans)

def inorder(l,tr,u,ans):
    if tr[u]:
        if tr[u][0][0] == 0:
            inorder(l, tr, tr[u][0][1], ans)
        ans.append(l[u])
        if tr[u][0][0] == 1:
            inorder(l, tr, tr[u][0][1], ans)
        elif len(tr[u]) == 2:
            inorder(l, tr, tr[u][1][1], ans)
    else:
        ans.append(l[u])

t=int(input())
l=list(map(int,input().split()))
tr=[[]for i in range(t)]
ans=[]
for j in range(t-1):
    tmp=list(map(int,input().split()))
    tr[tmp[0] - 1].append([tmp[1], j + 1])
inorder(l,tr,0,ans)
ans=[ans[i]-(i) for i in range(len(ans))]
print(len(ans)-finstr(ans,min(ans)-1,0))