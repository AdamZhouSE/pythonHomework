customers=list(map(int,input().split(",")))
grumpy=list(map(int,input().split(",")))
X=int(input())
calm=(0,X)
L=len(customers)
num=0
ans=0
for i in range(L):
    if grumpy[i]==0:
        num+=customers[i]
while calm[1]<=L:
    i,j=calm
    base=num
    for k in range(i,j):
        if grumpy[k]==1:
            base+=customers[k]
    ans=max(ans,base)
    calm=(i+1,j+1)
print(ans)