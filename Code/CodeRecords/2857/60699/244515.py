cnt=int(input())
list1=list(map(int,input().split(' ')))
res=1
for i in range(2,list1[0]):
    flag=True
    for j in list1:
        if j%i!=0:
            flag=False
            break
    if flag:
        res+=1
print(res)