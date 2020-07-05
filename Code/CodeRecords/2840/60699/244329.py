list1=list(map(int,input().split(' ')))
list2=list(map(int,input().split(' ')))
k=list1[1]
res=0
for i in list2:
    temp=0
    while i>0:
        if i%10==4 or i%10==7:
            temp+=1
        i//=10
    if temp<=k:
        res+=1
print(res)