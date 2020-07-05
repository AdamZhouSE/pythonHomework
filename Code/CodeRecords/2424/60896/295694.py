def find(list1,n):
    u=int(n/2)
    for i in range(0,u):
        if(list1[2*i]!=list1[2*i+1]):
            return 2*i
    if(n%2==0):
        return 0
    else:
        return n-1
    

a=eval(input())
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    list1.sort()
    index=find(list1,n)
    print(list1[index])