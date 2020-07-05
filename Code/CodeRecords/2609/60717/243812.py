n=int(input())

for i in range(0,n):
    list1=input().split()
    list2=input().split()
    list3=list2.copy()
    list4=[]
    flag=0
    for j in list2:
        list3.remove(j)
        if not(j in list3)and list3!=[]:
            flag=1
            list4.append(j)
        list3.append(j)

    try:
        print(list4[int(list1[1])-1])
    except:
        print(-1)
        