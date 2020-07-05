size=int(input())
ror=[]
for i in range(size):
    ror.append(list(map(int,input().split(' '))))
rmax=0
for i in range(size):
    sum=ror[i][0]+ror[i][1]
    rmax=max(rmax,sum)
print(rmax)
