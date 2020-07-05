num=int(input())
test=[]
res=[]
for i in range(num):
    test.append(input())
test=list(map(int,test))
for i in range(1,num+1):
    root=i
    count=0
    while test[root-1]!=-1:
        root=test[root-1]
        count+=1
    res.append(count)
    # while son!=root:
    #     test[root],son=son,test[root]
print(max(res)+1)