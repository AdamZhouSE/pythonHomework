t=int(input())
for i in range(0,t):
    a=input().split()
    l1=int(a[0])
    l2=int(a[1])
    arr1=input().split()
    arr2=input().split()
    res=set(arr1+arr2)
    print(len(res))
