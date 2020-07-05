a=eval(input())
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    dict1={}
    dep=0
    no=0
    for m in range(0,n):
        if(list1[m]in dict1):
            dep=list1[m]
        else:
            dict1[list1[m]]=list1[m]
    for m in range(1,n+1):
        if(not (m in dict1)):
            no=m
            break
    print(dep,no)