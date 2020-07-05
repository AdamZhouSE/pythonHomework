def index(list1,target):
    index1=-1
    for i in range(0,len(list1)):
        if list1[i]==target:
            index1=i
            break
    return index1

list1=list(map(int,input().split(",")))
target=int(input())
print(index(list1,target))