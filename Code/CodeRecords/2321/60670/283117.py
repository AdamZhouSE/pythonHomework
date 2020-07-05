def getndigit(x):
    cnt=0
    while x>0:
        cnt+=1
        x=x//10
    return cnt

def ntry(depth,x):
    if depth==ndigit:
        if x<=n:
            global ans
            ans+=1
            return
        else:
            global over
            over=True
    if over:
        return
    for i in range(0,num_of_D):
        ntry(depth+1,x*10+D[i])
        
D=list(map(int,input().split(',')))
n=int(input())
num_of_D=len(D)
ndigit=getndigit(n)
t=1
ans=0
over=False
for i in range(0,ndigit-1):
    t*=num_of_D
    ans+=t
print(ans)
ntry(ndigit,0)
print(ans)