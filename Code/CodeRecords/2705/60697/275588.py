res=eval(input())

leng=len(res)
degree=[0 for i in range(leng+1)]
for i in range(leng):
    degree[res[i][1]]+=1
def find(x,fa):
    while x != fa[x]:
        x = fa[x]
    return x
def helper(ex):
    fa=[i for i in range(leng+1)]
    cnt=leng
    for i in range(leng):
        if(ex==i):
            continue
        else:
            fx=find(res[i][0],fa)
            fy=find(res[i][1],fa)
            if(fx!=fy):
                cnt-=1
                fa[fy]=fx
    return cnt==1
i=leng-1
flag=False
fflag=False
while(i>=0):
    if(degree[res[i][1]]==2):
        if(helper(i)):
            print(res[i])
            flag=True
            break
    i-=1
i=leng-1
if(flag==False):
    while(i>=0):
        if(degree[res[i][1]]==1):
            if(helper(i)):
                print(res[i])
                fflag=True
                break
        i-=1
if(fflag==False and flag==False):
    print("[]")
