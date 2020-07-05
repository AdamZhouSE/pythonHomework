def isTriangle(lis):
    l=sorted(lis)
    if lis[2]-lis[0]<lis[1] and lis[0]+lis[1]>lis[2]:
        return True
    else:
        return False

x=input()
x=x[1:len(x)-1]
lis=list(map(int,x.split(",")))
ans=[]
for i in range(0,len(lis)-2):
    templis=[]
    for j in range(i,i+3):
        templis.append(lis[j])
    if isTriangle(templis):
        ans.append(templis[0]+templis[1]+templis[2])
if ans==[]:
    print(0)
else:
    print(max(ans))