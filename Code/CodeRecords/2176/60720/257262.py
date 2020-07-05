list1=list(input())
list0=[]

for i in range(len(list1)):
    list2=[list1[i],i+1]
    list0.append(list2)
list0.sort(key=lambda x:(x[0], -x[1]))
for i in range(len(list0)-1):
    print(list0[i][1],end=' ')
print(list0[len(list0)-1][1])
    