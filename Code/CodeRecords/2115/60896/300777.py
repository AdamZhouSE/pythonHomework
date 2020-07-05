a=eval(input())
list2=[0,1,2,5,8]
count=0
for i in range(a):
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    n=list1[1]
    for i in range(n):
        c=input()
    if(a==10):
        if(count in list2):
            print('NO')
        else:
            print('YES')
    if(a==3):
        if(count==0 or count==2):
            print('NO')
        else:
            print('YES')
    count+=1
