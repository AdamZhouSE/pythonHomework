num,l,r=map(int,input().split())
minnum=0
maxnum=0
for i in range(l):
    minnum+=pow(2,i)
for j in range(num-l):
    minnum+=1
for k in range(r):
    maxnum+=pow(2,k)
for s in range(num-r):
    maxnum+=pow(2,r-1)
print(minnum,end=" ")
print(maxnum)