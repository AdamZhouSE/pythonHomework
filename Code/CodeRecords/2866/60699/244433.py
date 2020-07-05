cnt=int(input())
list1 = list(map(int, input().split(' ')))
list2=[]
for i in range(0,len(list1)):
    if list1[i]==1:
        list2.append(i)
res=1
for i in range(1,len(list2)):
    res*=(list2[i]-list2[i-1])
print(res)