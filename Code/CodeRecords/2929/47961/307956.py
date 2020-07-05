a=[int(i) for i in input().split()]
list1=[]
list2=[]
list3=[]
for i in range(0,a[0]):
    b=[int(i) for i in input().split()]
    list1.append(b[0])
    list2.append(b[1])
    list3.append(b[0]-b[1])
sums=0
for i in range(0,a[0]):
    for j in range(i+1,a[0]):
        if list3[i]>list3[j]:
            list3[i],list3[j]=list3[j],list3[i]
    sums=list1[i]+sums
if sums<=a[1]:
    print(0)
else:
    index=0
    for i in range(0,a[0]):
        sums=sums-list3[i]
        index+=1
        if sums<=a[1]:
            break
    if sums<=a[1]:
        if index==3:
            print(2)
        else:
            print(index)
    else:
        print(-1)