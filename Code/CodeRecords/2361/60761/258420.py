def isSquare(x,seta,lista,n):
    for i in range(len(lista)):
        if seta[i]==x:
            lista[i]-=1
            break
    if(n==0):
        return 1
    else:
        ans=0
        for j in range(len(seta)):
            if(lista[j]>0 and (x+seta[j])**0.5==int((x+seta[j])/((x+seta[j])**0.5))):
                ans+=isSquare(seta[j],seta,lista[:],n-1)
        return ans
list0=list(map(int,input("").split(",")))
set1=list(set(list0))
list1=[]
for i in set1:
    list1.append(list0.count(i))
sum=0
for i in set1:
    sum+=isSquare(i,set1,list1[:],len(list0)-1)
print(sum)