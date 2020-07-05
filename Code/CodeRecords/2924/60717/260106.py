list1=input().split()
n=int(list1[0])
r=int(list1[1])
target=int(list1[2])*n
list1=[]
list2=[]
summ=0
count=0
for i in range(0,n):
    tmp=input().split()
    list1.append(int(tmp[0]))
    list2.append(int(tmp[1]))
    summ+=int(tmp[0])
if summ>=target:
    print(count)
else:
    while summ!=target:
        index=list2.index(min(list2))
        while list1[index]<r:
            list1[index]+=1
            count+=list2[index]
            summ+=1
            if summ==target:
                break
        list1.remove(list1[index])
        list2.remove(list2[index])
    print(count)