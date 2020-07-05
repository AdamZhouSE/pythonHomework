def findMin(list1):
    min1=list1[0]
    for i in range(0,len(list1)):
        if list1[i]<min1:
            min1=list1[i]
    return min1

list1=list(map(int,input().split(",")))
print(findMin(list1))