import sys
import re
n=100
f=[[0 for i in range(n)] for j in range(n)]
c=[["" for i in range(n)] for j in range(n)]
s=""
def judge(l,r,length):
    if (r-l+1)%length!=0:
        return 0
    else:
        for i in range(1,r-l+2):
            if s[l+i-1]!=s[l+(i-1)%length]:
                return 0
        return 1
def digit(num):
    ans=0
    while num>0:
        ans+=1
        num=num//10
    return ans
def solve( l, r):
    if f[l][r]:
        pass
    elif l==r:
        f[l][r]=1
        c[l][r]+=s[l]
    else:
        f[l][r]=r-l+1
        for i in range(l,r+1):
            c[l][r]+=s[i]
        for i in range(l,r):
            solve(l,i)
            solve(i+1,r)
            if f[l][r]>f[l][i]+f[i+1][r]:
                f[l][r]=f[l][i]+f[i+1][r]
                c[l][r]=c[l][i]+c[i+1][r]
        for i in range(1,r-l+1):
            if judge(l,r,i)==1:
                solve(l,l+i-1)
                if f[l][r]>f[l][l+i-1]+2+digit((r-l+1)//i):
                    f[l][r]=f[l][l+i-1]+2+digit((r-l+1)//i)
                    c[l][r]=str((r-l+1)//i)+"("+c[l][l+i-1]+")"
s=sys.stdin.read()
solve(0,len(s)-1)
print(c[0][len(s)-1])