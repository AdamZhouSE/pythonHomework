def indexofMin(arr):
    minindex = 0
    currentindex = 1
    while currentindex < len(arr):
        if arr[currentindex] < arr[minindex]:
            minindex = currentindex
        currentindex += 1
    return minindex
def fun(list1,list2):
    min=indexofMin(list2)
    if(min==0):
        count=0
        for i in range(0,len(list2)):
            count=count+list1[i]*list2[min]
        return count
    else:
        return fun(list1[0:min],list2[0:min])+fun(list1[min:],list2[min:])
n=int(input())
list1=[0]*n
list2=[0]*n
for i in range(0,n):
    temp=input().split()
    temp=list(map(int,temp))
    list1[i]=temp[0]
    list2[i]=temp[1]
print(fun(list1,list2))