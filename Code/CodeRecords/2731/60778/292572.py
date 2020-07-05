UCs=int(input())
for UC in range(UCs):
    size=int(input())
    goods=list(map(int,input().split()))
    goods.sort()
    p=0
    count=0
    while(p<size-1):
        if(goods[p]==goods[p+1]):
            count+=1
            p+=2
        else:
            p+=1
    print(count*2)