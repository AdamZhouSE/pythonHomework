num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split(" ")))
    count=1
    temp=0
    for j in range(0,n):
        if list1.count(list1[j])>count:
            temp=j
            count=list1.count(list1[j])
    if count==1:
        print("-1")
    else:
        print(temp+1)