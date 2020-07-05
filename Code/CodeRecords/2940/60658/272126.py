def dec(l,r):
    w = r-l+1
    for i in range(1,w//2+1):
        if w%i:continue
        if arr[l:r-i+1]==arr[l+i:r+1]:
            return i
    return -1

def dfs(l,r):
    if f[l][r]!=0:
        return f[l][r]
    if l==r:
        ss[l][r]=arr[l]
        f[l][r]=1
        return 1
    length = 9999999
    k = 0
    for i in range(l,r):
        ll = dfs(l,i)+dfs(i+1,r)
        if length>ll:
            length=ll
            k=i
    ss[l][r]=ss[l][k]+ss[k+1][r]
    f[l][r]=length
    d = dec(l,r)
    if d==-1:
        return f[l][r]
    sy = ""
    md = (r-l+1)//d
    sy+=str(md)
    sy = sy+"("+ss[l][l+d-1]+")"
    if len(sy)<f[l][r]:
        f[l][r]=len(sy)
        ss[l][r]=sy
    return f[l][r]
    
    

arr = input()
n = len(arr)
f = [[0 for i in range(n)]for j in range(n)]
ss = [["" for i in range(n)] for j in range(n)]
dfs(0,n-1)
print(ss[0][n-1])