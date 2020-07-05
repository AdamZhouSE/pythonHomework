cnt=int(input())
list1=list(map(int,input().split(' ')))
res=0
list2=[]
for i in range(1,list1[0]+1):
    if list1[0]%i==0:
        list2.append(i)
for i in list2:
    flag=True
    for j in list1:
        if j%i!=0:
            flag=False
            break
    if flag:
        res+=1
print(res)