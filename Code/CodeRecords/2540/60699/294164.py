list1=list(map(int,input().split(' ')))
list2=[]
for i in range(list1[0]):
    temp = list(map(int, input().split(' ')))
    list2.append(temp)
list2=sorted(list2,key=lambda x:(x[1],x[0]))
myd=[]
for i in range(list1[2]+1):
    myd.append(0)
ans=0
for i in range(1,list1[0]+1):
    myd.sort()
    j=1
    while j<=list1[2] and list2[i-1][2]!=0:
        if myd[j]<=list2[i-1][0]:
            ans+=1
            myd[j]=list2[i-1][1]
            list2[i-1][2]-=1
        j+=1
print(ans)