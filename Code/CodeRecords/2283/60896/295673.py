a=eval(input())
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    list1.sort()
    for i in range(0,n-1):
        print(list1[i],end=' ')
    print(list1[-1])
