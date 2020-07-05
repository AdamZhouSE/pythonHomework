def maxNum(list1):
    num=0
    for i in range(0,len(list1)):
        if(list1[i]>num):
            num=list1[i]
    return num

list1=list(map(int,input().split(",")))
x=maxNum(list1)
list1.remove(x)
y=maxNum(list1)
list1.remove(y)
z=maxNum(list1)
print(x*y*z)