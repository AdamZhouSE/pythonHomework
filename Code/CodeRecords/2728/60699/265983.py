cnt=int(input())
for i in range(0,cnt):
    n=int(input())
    list1=list(map(int,input().split(' ')))
    res=0
    for m in range(0,len(list1)-1):
        for n in range(m+1,len(list1)):
            res=max(res,(n-m)*min(list1[m],list1[n]))
    print(res)