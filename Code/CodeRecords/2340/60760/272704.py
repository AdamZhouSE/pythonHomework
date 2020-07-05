def func(arr:list): #实现功能的函数
    length=len(arr)
    arr2=[]
    for i in arr:
        arr2.append(i)
    arr2=func2(arr,arr2)
    arr=arr[::-1]  #反转
    arr2=arr2[::-1]#反转
    arr2=func2(arr,arr2)
    sum1=0     #通过计算两个数组的和的差来计算雨水储存
    sum2=0
    for i in arr:
        sum1=sum1+i

    for i in arr2:
        sum2=sum2+i
    return sum2-sum1

def func2(arr:list,arr2:list):       #完善数组的左边
    length = len(arr)
    left = arr[0]
    indexofleft = 0
    right = arr[length - 1]
    indexofright = length - 1
    for i in range(1, length):
        if arr[i] >= left:
            for j in range(indexofleft + 1, i):
                arr2[j] = left
            left = arr[i]
            indexofleft = i
    return arr2

tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
res=[]
for i in lists:
    res.append(func(i))
for i in res:
    print(i)
