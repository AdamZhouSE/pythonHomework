t=int(input())
size=26
str=input()
res=[[1 for i in range(26)] for j in range(26)]
def product(n,base):
    global ans
    while(n>0):
        if(n&1==1):
            matrix(ans,base)
        matrix(base,base)
        n=n>>1
def matrix(a,b):
    tmp=[[0 for i in range(size)] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(size):
                tmp[i][j]+=a[i][k]*b[k][j]
    for i in range(len(tmp)):
        for j in range(size):
            a[i][j]=tmp[i][j]
for i in range(t-1):
    res[ord(str[i])-ord('a')][ord(str[i+1])-ord('a')]=0
h=[[1 for i in range(size)]]
ans=[[0 for i in range(26)] for j in range(26)]
for i in range(26):
    ans[i][i]=1
product(t-1,res)
matrix(h,ans)
print(sum(h[0]))