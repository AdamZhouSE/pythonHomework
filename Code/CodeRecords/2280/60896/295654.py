a=eval(input())
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    for i in range(1,n+1):
        if(i not in list1):
            print(i)
            break