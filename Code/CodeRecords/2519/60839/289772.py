def isTriangle(lis):
    l=sorted(lis)
    if l[2]-l[0]<l[1] and l[0]+l[1]>l[2]:
        return True
    else:
        return False

x=input()
x=x[1:len(x)-1]
lis=list(map(int,x.split(",")))
ans=[]
for i in range(0,len(lis)-2):
    for j in range(i+1,len(lis)-1):
        for k in range(j+1,len(lis)):
            templis = []
            templis.append(lis[i])
            templis.append(lis[j])
            templis.append(lis[k])
            if isTriangle(templis):
                ans.append(templis[0]+templis[1]+templis[2])
if ans==[]:
    print(0)
else:
    print(max(ans))