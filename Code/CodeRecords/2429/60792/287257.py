num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split(" ")))
    count=-1
    for j in range(0,n):
        for k in range(j+1,n):
            if list1[k]-list1[j]>count:
                count=list1[k]-list1[j]
    print(count)            