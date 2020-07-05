a=eval(input())
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    result=list1[0]
    tem2=0
    tem1=0#记录前n-1项的和
    for i in range(1,n):
        j=list1[i]
        tem2=result
        result=max(result,tem1+j)
        tem1=tem2
    print(result)