str1=input()
def judge(x1,y1,x2,y2,s):
    len1=y1-x1+1
    len2=y2-x2+1
    if len2%len1:
        return 0
    for i in range(x2,y2+1):
        if s[i]!=s[i-len1]:
            return 0
    return 1
def work(x):
    ans=0
    while x:
        x=x//10
        ans+=1
    return ans
def minlen(s):
    n=len(s)
    f=[([0]*n) for _ in range(n)]
    for i in range(0,n):
        for j in range(i,n):
            f[i][j]=j-i+1
    for len1 in range(1,n):
        for i in range(0,n-len1):
            j=i+len1
            for k in range(i,j):
                if judge(i,k,k+1,j,s)==0:
                    f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j])
                else:
                    f[i][j]=f[i][j]=min(f[i][j],f[i][k]+work((len1+1)/(k-i+1))+2)
    return f[0][n-1]
print(minlen(str1))