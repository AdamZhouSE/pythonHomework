def isSquare(x,list1,n):
    if(n==0):
        if(x**0.5==int(x/(x**0.5))):
            return 1
        else:
            return 0
    else:
        ans=0
        for num in list1:
            if(num[1]>0 and (x+num[0])**0.5==int((x+num[0])/((x+num[0])**0.5))):
                list1[list1.index(num)][1]-=1
                ans+=isSquare(num[0],list1,n-1)
        return ans
list0=list(map(int,input("").split(",")))
set1=list(set(list0))
list1=[]
for i in set1:
    list1.append([i,list0.count(i)])
sum=0
for i in range(len(set1)):
    list1[i][1]-=1
    sum+=isSquare(list1[i][0],list1,len(list0)-1)
    list1[i][1]+=1
print(sum)