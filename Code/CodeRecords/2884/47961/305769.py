list1=[int(i) for i in input().split()]
list2=[int(i) for i in input().split()]
index=0
if list1[0]!=1:
    for i in range(0,list1[0]):
        for j in range(i+1,list1[0]):
            if abs(list2[i]-list2[j])<=list1[1]:
                index+=1
else:
    index=0
index=index*2
print(index)