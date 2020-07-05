lis=input().split(" ")
m=int(lis[0])
q=int(lis[1])
stone=list(map(int,input().split(" ")))
stone=sorted(stone,reverse=True)
ans=[]
for i in range(0,q):
    lis1=list(map(int,input().split(" ")))
    if lis1[0]==1:
        ans.append(stone[lis1[1]-1])
    else:
        stone.append(lis1[1]-1)
        stone=sorted(stone,reverse=True)
for i in ans:
    print(i)