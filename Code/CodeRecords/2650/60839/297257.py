def func(lis,dogs):
    temp=[]
    for i in range(lis[0]-1,lis[1]):
        temp.append(dogs[i])
    temp=sorted(temp)
    return temp[lis[2]-1]

lis=list(map(int,input().split(" ")))
n=lis[0]
m=lis[1]
dogs=list(map(int,input().split(" ")))
ans=[]
for i in range(0,m):
    lis1=list(map(int,input().split(" ")))
    ans.append(func(lis1,dogs))
for i in ans:
    print(i)