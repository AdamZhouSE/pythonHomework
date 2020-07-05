def findRoadLen(index):
    if pre[index]==0:
        return 0
    else:
        return 1 + findRoadLen(pre[index])
def find(x,y,leaves):
    if pre[x]==pre[y] and x in leaves and y in leaves: return 2
    if pre[x]==pre[y]==0:return 0
    if pre[x]==pre[y] and pre[x]!=0:return 2
    if pre[x]==0:
        return find(x,pre[y],leaves)+1
    elif pre[y]==0:
        return find(pre[x],y,leaves)+1
    else:
        return find(pre[x],pre[y],leaves)+2

n=int(input())
pre=[]
roads=[]
leaves=[]
for i in range(n+1):pre.append(0)
for i in range(n-1):
    s=input().split(" ")
    pre[int(s[1])]=int(s[0])
for i in range(1,n+1):
    if i not in pre:
        leaves.append(i)

if len(leaves)==1:
    print(findRoadLen(leaves[0]))
else:
    for i in range(len(leaves)-1):
        for j in range(i+1,len(leaves)):
            roads.append(find(leaves[i],leaves[j],leaves))
    res=max(roads)
    print(res)