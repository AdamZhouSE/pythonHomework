n=int(input())
for i in range(0,n):
    m=int(input())
    list1=input().split()
    flag=0
    for j in range(0,m):
        summ=0
        for k in range(j,m):
            summ+=int(list1[k])
            if summ==0:
                flag=1
    if flag==1:
        print('Yes')
    else:
        print('No')