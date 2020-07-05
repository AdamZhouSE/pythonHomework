testNum=int(input())
for i in range (testNum):
    srcs=input().split(' ')
    m=int(srcs[0])
    n=int(srcs[1])
    arr1=input().split(' ')
    arr2=input().split(' ')
    bo=True
    for item in arr2:
        if(item not in arr1):
            bo=False
            break
        else:
            if(arr2.count(item)>arr1.count(item)):
                bo=False
                break
    if(bo):print('Yes')
    else:print('No')