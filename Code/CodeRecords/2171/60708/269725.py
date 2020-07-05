N=int(input())
for n in range(0,N):
    l=int(input())
    temp=input().split(" ")
    list0=[]
    for item in temp:
        list0.append(int(item))
    list1=[]
    list2=[]
    for item in list0:
        if item%2==0:
            list2.append(item)
        else:
            list1.append(item)
    for item in list2:
        print(item,end=" ")
    for item in list1:
        print(item,end=" ")
    print("")
