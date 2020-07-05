n,d=map(int,input().split())
l=list(map(int,input().split()))
index=0
for i in range(0,len(l)-1):
    if l[i]>=l[i+1]:
        while l[i]>=l[i+1]:
            index+=1
            l[i+1]+=d
print(index)