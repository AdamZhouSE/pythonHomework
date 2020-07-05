import sys
maxn=100005
sum=[0 for i in range(maxn)]
s=[]
idx=0
def bulid(p):
    global idx,sum
    v=s[idx]
    idx+=1
    if v==-1:
        return
    sum[p]+=v
    bulid(p-1)
    bulid(p+1)
def init():
    global idx,sum
    v=s[idx]
    idx+=1
    if v==-1:
        return -1
    sum=[0 for i in range(maxn)]
    p=maxn//2
    sum[p]=v
    bulid(p-1)
    bulid(p+1)
    return 1
case=0
lines=sys.stdin.readlines()
for i in lines:
    line=i.strip()
    tmp=list(map(int,line.split()))
    s+=tmp
k=0
try:
    while init()==1:
        p = 0
        while sum[p] == 0:
            p += 1
        k += 1
        print("Case", k, end="")
        print(":")
        while sum[p+1] != 0:
            print(sum[p], end=" ")
            p += 1
        print(sum[p])
        print()
except:
    a=1