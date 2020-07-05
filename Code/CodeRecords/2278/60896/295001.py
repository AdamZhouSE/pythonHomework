a=eval(input())    
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    list2=[]
    for i in range(0,n-1):
        list2.append(list1[i]^list1[i+1])
    list2.append(list1[n-1])
    for i in range(0,len(list2)-1):
        print(list2[i],end=' ')
    print(list2[-1])
