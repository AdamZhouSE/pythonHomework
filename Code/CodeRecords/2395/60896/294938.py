a=eval(input())    
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    for i in range(0,n-1):
        if(not list1[i]==0):
            if(list1[i+1]==list1[i]):
                list1[i+1]=0
                list1[i]=list1[i]*2
    for i in range(0,n):
        list1.remove(0)
        list1.append(0)
    for i in range(0,len(list1)-1):
        print(list1[i],end=' ')
    print(list1[-1])

