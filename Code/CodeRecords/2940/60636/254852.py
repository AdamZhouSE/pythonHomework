def judge(l,r,length,s):
    if (r-l+1)%length:
        return 0
    for i in range(1,r-l+2):
        if(s[l+i-1]!=s[l+(i-1)%length]):
            return 0
    return 1
def digit(num):
    ans=0
    while(num):
        ans=ans+1
        num=num/10
    return ans
def change(num):
    s=""
    while(num):
        s=s+(num%10+48)
        num=num/10
    a=list(s)
    for i in range(len(s)/2):
        c=a[i]
        a[i]=a[len(a)-i-1]
        a[len(a)-i-1]=c
    return a.tostring()
def solve(l,r,f,c,s):
    print(c)
    if(f[l][r]):
        return
    if(l==r):
        f[l][r]=1
        c[l][r]=c[l][r]+s[l]
        return
    f[l][r]=r-l+1
    for i in range(l,r+1):
        c[l][r]=c[l][r]+s[i]
    for i in range(l,r):
        solve(l,i,f,c,s)
        solve(i+1,r,f,c,s)
        if(f[l][r]>f[l][i]+f[i+1][r]):
            f[l][r]=f[l][i]+f[i+1][r]
            c[l][r]=c[l][i]+c[i+1][r]
    for i in range(1,r):
        if(judge(l,r,i,s)):
            solve(l,l+i-1,f,c,s)
            if(f[l][r]>f[l][l+i-1]+2+digit((r-l+1)/i)):
                f[l][r]=f[l][l+i-1]+2+digit((r-l+1)/i)
                c[l][r]=change((r-l+1)/i)+"("+c[l][l+i-1]+")"
source=list(input())
n=len(source)
f=[]
for i in range(n):
    fs=[]
    for j in range(n):
        fs.append(0)
    f.append(fs)
c=[]
for i in range(n):
    cs=[]
    for j in range(n):
        cs.append("")
    c.append(cs)
solve(0,n-1,f,c,source)
print(c[0][n-1])




































