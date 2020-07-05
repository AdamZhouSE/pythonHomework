customer=list(map(int,input().split(",")))
copy=customer.copy()
grumpy=list(map(int,input().split(",")))
x=int(input())
N=len(customer)
m=0
for i in range(N):
    if grumpy[i]==0:
        copy[i]=0
for j in range(N-x+1):
    m=max(sum(copy[j:j+x]),m)
for k in range(N):
    if grumpy[k]==1:
        customer[k]=0
print(str(m+sum(customer)))
    
