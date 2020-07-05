def find(list1):
    length = len(list1)
    l=0
    r = length
    while(l < r):
        mid = int((l + r + 1)/2)
        if(list1[length - mid] >= mid):
            l = mid
        else:
            r = mid - 1
    return l


temp=input().split(',')
b=map(eval,temp)
list1=list(b)
print(find(list1))
