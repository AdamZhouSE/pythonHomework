a=eval(input())
for i in range(0,a):
    temp=input().split(' ')
    n=eval(temp[0])
    x=eval(temp[1])
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    boo=False
    for i in range(0,n-1):
        num1=list1[i]
        for m in range(i+1,n):
            num2=list1[m]
            if(num1+num2==x):
                boo=True
    if(boo):print("Yes")
    else:print("No")