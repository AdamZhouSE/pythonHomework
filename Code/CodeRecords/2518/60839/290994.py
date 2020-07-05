x=input()
y=input()

lis1=list(map(int,x.split(",")))
lis2=list(map(int,y.split(",")))
lis2.append(1)
lis2.append(len(lis1))
lis2=sorted(lis2)
ans=[]
for i in range(0,len(lis2)-1):
    ans.append((lis2[i+1]-lis2[i]-1)//2)
print(max(ans))
