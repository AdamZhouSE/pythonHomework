n=int(input())
l=[0 for i in range(n)]
v=[0 for i in range(n)]

res=[]

for i in range(n*n):
    temp=list(map(int,input().split(" ")))
    if(l[temp[0]-1]==0 and v[temp[1]-1]==0):
        l[temp[0] - 1] = 1
        v[temp[1] - 1] = 1
        res.append(i+1)
i=0
while(i<len(res)):
    if(i!=0):
        print(" ",end="")
    print(res[i],end="")
    i+=1
print()