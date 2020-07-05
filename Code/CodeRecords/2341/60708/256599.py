N=eval(input())
for n in range(0,N):
    tempstr=input().split(" ")
    l1=int(tempstr[0])
    l2=int(tempstr[1])
    list=input().split(" ")
    list1=[]
    for item in list:
        list1.append(int(item))
    list = input().split(" ")
    list2=[]
    for item in list:
        list2.append(int(item))

    for item in list2:
        list1.append(item)
    list1=sorted(list1)
    for item in list1:
        print(item,end=" ")
    print("")