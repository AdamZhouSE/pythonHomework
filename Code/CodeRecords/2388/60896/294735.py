a=eval(input())    
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    temp=input().split(' ')
    b=map(eval,temp)
    list2=list(b)
    list1.sort()
    list2.sort()
    if(list1==list2):
        print(1)
    else:
        print(0)
