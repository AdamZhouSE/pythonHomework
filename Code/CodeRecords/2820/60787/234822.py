n=int(input())
list1=[]
list2=[]
for i in range(0,n):
    temp=[int(x) for x in input().split(" ")]
    if temp in list1:
        list2[list1.index(temp)]+=1
    else:
        list1.append(temp)
        list2.append(1)
print(max(list2))