a=eval(input())
for i in range(a):
    n=eval(input())
    temp=input().split(' ')
    temp=map(eval,temp)
    list1=list(temp)
    list2=[]
    list3=[]
    for i in list1:
        if(i%2==0):
            list2.append(i)
        else:
            list3.append(i)
    for i in list2:
        print(i,end=' ')
    for i in list3:
        print(i,end=' ')
    print('')