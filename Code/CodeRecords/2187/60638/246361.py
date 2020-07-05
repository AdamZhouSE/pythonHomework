num=int(input())
for x in range(0,num):
    list1=list(map(int , input().split(" ")))
    list2=list(map(int , input().split(" ")))
    maxn=0
    for i in range(0,len(list2)-list1[1]+1):
        sum=0
        for j in range(i,i+list1[1]):
            sum=sum+list2[j]
        maxn=max(sum,maxn)
    print(maxn)