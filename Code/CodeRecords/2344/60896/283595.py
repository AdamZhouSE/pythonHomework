a=eval(input())
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    d=eval(input())
    list2=list1[0:d]
    list3=list1[d:n]
    result=list3+list2
    for t in range(0,n):
        print(result[t],end=' ')
    print('')