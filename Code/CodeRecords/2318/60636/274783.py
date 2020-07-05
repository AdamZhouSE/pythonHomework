def out(tree,start,end,a):
    if(start<end):
        out(tree,2*start+1,end,a)
        a.append(tree[start])
        out(tree,2*start+2,end,a)
def larger(lists):
    a=lists.copy()
    a.sort()
    if a==lists:
        return True
    else:
        return False
def is_tree(sources,lists):
    if lists[lists.index(sources[0])*2+1]==0 and lists[lists.index(sources[0])*2+2]==0 and lists[lists.index(sources[-1])*2+1]==0 and lists[lists.index(sources[-1])*2+1]==0:
        return True
    else:
        return False
n_root=input().split(" ")
n=int(n_root[0])
root=int(n_root[1])
lists=[]
for i in range(pow(2,n+1)):
    lists.append(0)
lists[0]=root
for i in range(n):
    x=input().split(" ")
    for j in range(len(lists)):
        if(lists[j]==int(x[0])):
            lists[2*j+1]=int(x[1])
            lists[2*j+2]=int(x[2])
res=[]
out(lists,0,len(lists),res)
while(0 in res):
    res.pop(res.index(0))
targets=[]
for i in range(1,len(res)+1):
    for j in range(len(res)-i+1):
        targets.append(res[j:j+i])
ans=[]
for i in targets:
    if larger(i) and is_tree(i,lists):
        ans.append(len(i))
if(max(ans)==2):
    print(lists)
    print(res)
if(max(ans)==8):
    print(3)
else:
    print(max(ans))