n,r=map(int,input().split())
num=list(map(int,input().split()))
num.sort(reverse=True)
require=[0 for i in range(n)]
for i in range(r):
    a,b=map(int,input().split())
    for i in range(a-1,b):
        require[i]+=1
require.sort(reverse=True)
out=0
for i in range(0,len(require)):
    out+=require[i]*num[i]
print(out)