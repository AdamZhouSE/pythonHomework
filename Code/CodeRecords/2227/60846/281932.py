def crackSafe(n,k):
    ans=""
    if n==1:
        for i in range(k): ans+= str(i)
        return ans

    vis={}
    ret=[]
    src="0"*(n-1)
    dfs(src,vis,ret,k)
    for i in range(len(ret)-1,-1,-1):
        if i==len(ret)-1: ans=ret[i]
        else: ans+=ret[i][-1]
    return ans
def dfs(src,vis,ret,k):
    tmp=src[1:]
    for i in range(k):
        dest=tmp+str(i)
        if src not in vis:
            vis[src]=set()   #vis[src]={}说明是字典！！而不是集合
        if dest not in vis[src]:
            vis[src].add(dest)
            dfs(dest,vis,ret,k)
            ret.append(src+str(i))
print(crackSafe(int(input()),int(input())))