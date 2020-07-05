def index(list1,target):
    list2=[]
    index1=-1
    index2=-1
    for i in range(0,len(list1)):
        if list1[i]==target:
            index1=i
            break
    if index1!=-1:
        for i in range(index1,len(list1)):
            if list1[i]==target:
                index2=i
    list2.append(index1)
    list2.append(index2)
    return list2

list1=list(map(int,input().split(",")))
target=int(input())
print(index(list1,target))