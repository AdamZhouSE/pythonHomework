num=int(input())
l=list(map(int,input().split()))
localMax=0
localMin=0
for i in range(1,num-1):
    if l[i-1]<l[i] and l[i]>l[i+1]:
        localMax+=1
    if l[i-1]>l[i] and l[i]<l[i+1]:
        localMin+=1
print(localMin+localMax)