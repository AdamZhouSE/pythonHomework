cnt=int(input())
for i in range(0,cnt):
    list1=list(map(int, input().split(' ')))
    num1=list1[0]
    num2=list1[1]
    res1=0
    res2=0
    index=1
    while num1>0:
        res1+=(num1%10)*index
        num1//=10
        index*=2
    index=1
    while num2>0:
        res2+=(num2%10)*index
        num2//=10
        index*=2
    print(res1*res2)