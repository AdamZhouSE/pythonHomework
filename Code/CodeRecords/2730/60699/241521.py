cnt=int(input())
for i in range(0,cnt):
    input()
    list1=list(map(int,input().split(" ")))
    res=0
    for temp in list1:
        while temp>0:
            res+=temp%10
            temp//=10
    if res%3==0:
        print(1)
    else:
        print(0)