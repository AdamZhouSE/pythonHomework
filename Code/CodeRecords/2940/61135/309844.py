def DFS(l,r):
    if(l==r): return "".join(s[l:l+1])
    if(len(f[l][r])>0): return f[l][r]
    f[l][r]="".join(s[l:l+r-l+1])
    for i in range(l,r):
        if (len(f[l][r])>(len(DFS(l,i))+len(DFS(i+1,r)))):
            f[l][r]=DFS(l,i)+DFS(i+1,r)
    for i in range(l,r):
        if (check(l,i,i+1,r)==1): 
            strtemp=str(int((r-l+1)/(r-i)))+"("+DFS(i+1,r)+")"
            if (len(f[l][r]) > len(strtemp)):
                f[l][r] = strtemp
    return f[l][r]
def check(l,r,L,R):
    if ((r-l+1)%(R-L+1)!=0): return 0
    for i in range(l,r+1):
        if(s[i]!=s[(i-l)%(R-L+1)+L]): return 0
    return 1
s=list(input())
leng=len(s)
f=[] 
for i in range(100):
    f.append([""]*(100))
print(DFS(0,leng-1))