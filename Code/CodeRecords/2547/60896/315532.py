a=eval(input())
for i in range(a):
    n=eval(input())
    temp=input().split(' ')
    temp=map(eval,temp)
    list1=list(temp)
    k=eval(input())
    list2=[]
    for i in range(n-1):
        x=list1[i]
        for j in range(i+1,n):
            y=list1[j]
            if(x-y==k ):
                if([x,y] not in list2):
                    list2.append([x,y])
            if(y-x==k):
                if([y,x] not in list2):
                    list2.append([y,x])
    print(len(list2))