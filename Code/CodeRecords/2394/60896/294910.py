a=eval(input())    
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    result=list1
    for i in range(0,n):
        if(list1[i]==0):
            result.remove(0)
            result.append(0)
    for i in range(0,len(list1)):
        print(list2[i],end=' ')
    print('')
