n,x=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(enumerate(l),key=lambda x:x[1])
sum=0
for i,j in l:
    sum+=j*max(1,x-i)
print(sum)