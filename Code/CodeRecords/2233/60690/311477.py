def dfs(this,spy,key):
    count=0
    for j in range(len(spy[key])):
        if spy[key][j]==1 and j not in this:
            this.append(j)
            count+=1
            dfs(this,spy,j)
    if count==0:return

N=int(input())
spy=[]
for i in range(N):
    s=input().split(" ")
    for j in range(N):
        s[j]=int(s[j])
    spy.append(s)
dict={}
for i in range(N):
    dict[i]=[]
for key in dict.keys():
    this=[]
    dfs(this,spy,key)
    for e in this:
        dict[key].append(e)
    dict[key].sort()
pure=[]
for key in dict.keys():
    if dict[key] not in pure:
        pure.append(dict[key])
for i in range(len(pure)-1):
    for j in range(i+1,len(pure)):
        if pure[i]!=[] and pure[j]!=[]:
            if set(pure[i])>=set(pure[j]):
                pure[j]=[]
            elif set(pure[i])<=set(pure[j]):
                pure[i]=[]
while [] in pure:pure.remove([])
print(len(pure))