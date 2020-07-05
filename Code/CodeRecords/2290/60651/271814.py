n=int(input())
for i in range(n):
    l=int(input())
    list1=input().split()
    list1=[int(x) for x in list1]
    list2=[]
    for j in range(l-1):
        if list1[j]>list1[j+1]:
            list2.append(list1[j+1])
        else:
            list2.append(-1)
    list2.append(-1)
    list2=[str(x) for x in list2]
    print(" ".join(list2),end="")
    print(" ")
        