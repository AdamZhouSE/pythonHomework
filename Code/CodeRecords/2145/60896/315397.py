a=eval(input())
for i in range(a):
    n=eval(input())
    list1=[0 for i in range(n)]
    temp=input().split(' ')
    temp=map(eval,temp)
    list2=list(temp)
    for i in range(n):
        count=1
        for j in range(i-1,-1,-1):
            if(list2[j]<list2[i]):break
            count+=1
        for j in range(i+1,n):
            if(list2[j]<list2[i]):break
            count+=1
        list1[i]=count
    max1=0
    for i in range(n):
        if(list1[i]*list2[i]>max1):
            max1=list1[i]*list2[i]
    print(max1)