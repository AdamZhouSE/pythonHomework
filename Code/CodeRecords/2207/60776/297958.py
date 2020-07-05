a=int(input())
for k in range(0,a):
    a=input().split(' ')
    m=int(a[0])
    n=int(a[1])
    list=[]
    for i in range(1,n+1):
        list.append(i)
    if sum(list)>m:
        print(0)
    else:
        print(1)